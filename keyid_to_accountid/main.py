import os
import mesop as me
import mesop.labs as mel
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

import base64
import binascii

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

def keyid_to_accountid(sText):
    try:
        logging.info("Starting keyid_to_accountid function")
        #
        sText = sText.strip()
        # Example usage
        #example_input = sText # "ASIAQNZGKIQY56JQ7WML"
        result = validate_string(sText)
        print(f"Is '{sText}' valid? {result}")
        #
        sResult = "!E55OR!"
        if result:
            result = AWSAccount_from_AWSKeyID(sText)
            sResult = str("{:012d}".format(result))
        else: 
            sResult = "Invalid Input :\\"
        sResult = str(result)
        #
        return sResult
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}", exc_info=True)
        return f"An unexpected error occurred: {str(e)}"

@me.page(path="/", title="AWS KEY ID to AWS Account ID")
def app():
    mel.text_to_text(
        keyid_to_accountid,
        title="Decode AWS KEY ID to obtain the AWS Account ID.",
    )
    me.code("""Examples:
            
ASIAQNZGKIQY56JQ7WML -> 29608264753
ASIAY34FZKBOKMUTVV7A -> 609629065308
AKIASP2TPHJSQH3FJXYZ -> 171436882533
AKIAVJTCYHPL6QWFVZ4Q -> 364205587415
AKIA6ODU5DHT7HGWSLU5 -> 992382622183
            """)
    me.divider()
    me.code("""Honey Tokens:
            
CanaryTokens // canarytokens.org // canarytokens.com
052310077262
171436882533
534261010715
595918472158
717712589309
819147034852
992382622183

            
???
044858866125
251535659677
344043088457
351906852752
390477818340
426127672474
427150556519
439872796651
445142720921
465867158099
637958123769
693412236332
732624840810
735421457923
959235150393
982842642351 


SpaceSiren // https://github.com/spacesiren/spacesiren/tree/master
            
SpaceCrab // https://bitbucket.org/asecurityteam/spacecrab/src/master/
            """)
    me.divider()
    me.code("""References:
            
 - https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html
 - https://summitroute.com/blog/2018/06/20/aws_security_credential_formats/
 - https://github.com/danzek/aws-account-id-from-key-id
 - https://hackingthe.cloud/aws/enumeration/get-account-id-from-keys/
 - https://medium.com/@TalBeerySec/a-short-note-on-aws-key-id-f88cc4317489
 - https://trufflesecurity.com/blog/research-uncovers-aws-account-numbers-hidden-in-access-keys
 - https://github.com/trufflesecurity/trufflehog/blob/main/pkg/detectors/aws/aws.go
            """)

if __name__ == "__main__":
    logging.info("Application started")