import os
import mesop as me
import mesop.labs as mel
import time
import logging
import requests
from requests_aws4auth import AWS4Auth

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

import base64
import binascii

def AwsUsername_from_AwsCreds(sAwsAccessKeyId, sAwsSecretAccessKey):
    sReturn = "E55OR"
    
    # Request details
    region = 'us-east-1'
    service = 'sqs'
    url = 'https://sqs.us-east-1.amazonaws.com/'
    payload = {'Action': 'ListQueues'}
    
    # Create AWS4Auth instance
    auth = AWS4Auth(sAwsAccessKeyId, sAwsSecretAccessKey, region, service)
    
    # Custom User-Agent string
    sUserAgent = "Boto3/1.17.46 Python/3.6.14 Linux/4.14.238-182.422.amzn2.x86_64 exec-env/AWS_ECS_FARGATE Botocore/1.20.46"

    # Create headers dictionary with custom User-Agent
    headers = {
        "User-Agent": sUserAgent
    }

    # Make the request
    response = requests.post(url, auth=auth, params=payload, headers=headers)

    # Print the response
    print("[~] response.text:")
    print(response.text)

    sText = str(response.text)

    # ###

    sub_string = "User:"
    position = sText.find(sub_string)

    if position != -1:
        print(f"[~]'{sub_string}' found at index {position}")
    else:
        print(f"[!]'{sub_string}' not found in the string")
        exit()

    position = position + len(sub_string) + 1
    sTextWipOne = str(sText[position:])
    #print(sTextWipOne)
    # Split the response text by spaces
    lTextWipTwo = sTextWipOne.split(' ')
    sTextWipTwo = lTextWipTwo[0]
    print("[+] " + sub_string)
    print(sTextWipTwo)
    sReturn = sTextWipTwo
    return sReturn

def AWSAccount_from_AWSKeyID(AWSKeyID):
    
    trimmed_AWSKeyID = AWSKeyID[4:] #remove KeyID prefix
    x = base64.b32decode(trimmed_AWSKeyID) #base32 decode
    y = x[0:6]
    
    z = int.from_bytes(y, byteorder='big', signed=False)
    mask = int.from_bytes(binascii.unhexlify(b'7fffffffff80'), byteorder='big', signed=False)
    
    e = (z & mask)>>7
    return (e)

# print ("account id:" + "{:012d}".format(AWSAccount_from_AWSKeyID("ASIAQNZGKIQY56JQ7WML")))

def validate_string(input_string):
    valid_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ234567")
    
    # Check if the string is exactly 20 characters long
    if len(input_string) != 20:
        return False
    
    # Check if the first 4 characters are letters
    if not input_string[:4].isalpha():
        return False
    
    # Check if all characters are valid
    if not all(char in valid_chars for char in input_string):
        return False
    
    return True

def keyid_to_username(sTextOne, sTextTwo):
    try:
        logging.info("Starting keyid_to_accountid function")
        #
        sAwsAccessKeyId = sTextOne.strip()
        sAwsSecretAccessKey = sTextTwo.strip()
        # Example usage
        #example_input = sText # "ASIAQNZGKIQY56JQ7WML"
        result = validate_string(sAwsAccessKeyId)
        print(f"Is '{sAwsAccessKeyId}' valid? {result}")
        #
        sResult = "!E55OR!"
        if result:
            resultOne = AWSAccount_from_AWSKeyID(sAwsAccessKeyId)
            sAwsAccountNumber = str("{:012d}".format(resultOne))
            print(f"Account ID: {sAwsAccountNumber}")
            resultTwo = AwsUsername_from_AwsCreds(sAwsAccessKeyId, sAwsSecretAccessKey)
            result = resultTwo
        else: 
            sResult = "Invalid Input :\\"
        sResult = str(result)
        #
        return sResult
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}", exc_info=True)
        return f"An unexpected error occurred: {str(e)}"

@me.stateclass
class State:
  input_one: str = ""
  input_two: str = ""
  output_one: str = ""

def button_click(event: me.ClickEvent):
  state = me.state(State)
  sInputOne = str(state.input_one)
  sInputTwo = str(state.input_two)
  sOutputOne = keyid_to_username(sInputOne, sInputTwo)
  state.output_one = sOutputOne

#def on_click(e: me.SelectSelectionChangeEvent):
#  s = me.state(State)
#  s.selected_values = e.values

#def process_inputs(value1, value2):
#    me.markdown(f"Received inputs: {value1} and {value2}")

def on_blur_one(e: me.InputBlurEvent):
  state = me.state(State)
  print("e: " + str(e))
  print("state: " + str(state))
  state.input_one = e.value
  print("state.input_one: " + str(state.input_one))

def on_blur_two(e: me.InputBlurEvent):
  state = me.state(State)
  state.input_two = e.value
  print("state.input_two: " + str(state.input_two))

@me.page(path="/", title="AWS KEY ID to AWS Account ID")
def app():
    state = me.state(State)
    me.text(f"WhoAmi without CloudTrail Logging", type="headline-5")
    me.text(f"(AWS Access Key ID + AWS Secret Access Key) to AWS IAM Username", type="headline-6")
    me.divider()
    me.input(label="AWS Access Key ID", on_blur=on_blur_one, type='text', placeholder="AKIA___EXAMPLE___YTI", hint_label="AKIA___EXAMPLE___YTI")
    #me.text(text=state.input_one)
    me.divider()
    me.input(label="AWS Secret Access Key", on_blur=on_blur_two, placeholder="RKmA___EXAMPLE___TiSbaySIgcCTC9wklTTNzFA", hint_label="RKmA___EXAMPLE___TiSbaySIgcCTC9wklTTNzFA")
    #me.text(text=state.input_two)
    me.divider()
    me.button("Go!", type="raised", on_click=button_click)
    me.text(text="This Leverages an AWS API Endpoint for SQS with the Action of ListQueues, which lacks CloudTrail logging as of 20240708 and returns the username associated with the credentials as part of the error messaging that is return from the api endpoint when the user does not have access to the SQS service. See the AWS docs and references below for more information.", type="caption")
    me.divider()
    me.text(f"AWS IAM Username: {state.output_one}")    
    me.divider()
    me.code("""NOTE:

- Thinkst Canarytokens can still get you caught, albiet the alert is typically delay by a few hours, and the alert does NOT have your IP address.
- AWS has a backup mechanism for identifying credential usage. This is NOT related to CloudTrail logging.
- The IAM service lets you generate and download a report for all your credentials.
- This is a CSV file where each row belongs to an IAM user, and some of the columns identify when an access key was used, and on which AWS service it was used.
            """)
    me.divider()
    me.code("""References:

- https://blog.thinkst.com/2022/02/a-safety-net-for-aws-canarytokens.html
- https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html
- https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-logging-using-cloudtrail.html
- https://hackingthe.cloud/aws/enumeration/whoami/
- https://i.blackhat.com/BH-US-23/Presentations/US-23-Frichette-Evading-Logging-in-the-Cloud-Bypassing-AWS-CloudTrail.pdf
- https://www.youtube.com/watch?v=YP2XNAbB_Nw
- https://www.youtube.com/watch?v=OraWbzAn5A8
- https://www.youtube.com/watch?v=61C_lEQ5qNM
- https://frichetten.com/blog/aws-api-enum-vuln/
- https://github.com/Frichetten/aws_stealth_perm_enum
            """)

if __name__ == "__main__":
    logging.info("Application started")