import boto3
import string
import secrets
import random
import time
import json

def _31337_effect():
    characters = "10"
    quote_line = 50
    quote = " pool on the roof must have a leak "
    line_width = 80
    padding_length = (line_width - len(quote)) // 2
    for i in range(100):
        if i == quote_line:
            padding = ''.join(random.choice(characters) for _ in range(padding_length))
            print(padding + quote + padding)
        else:
            line = ''.join(random.choice(characters) for _ in range(line_width))
            print(line)
        time.sleep(0.05)  # Reduced sleep time for faster scrolling

def generate_random_string(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for i in range(length))

def generate_random_password(length=26):
    if length < 26:
        raise ValueError("Password length must be at least 26 characters")
    
    uppercase = ''.join(secrets.choice(string.ascii_uppercase) for _ in range(1))
    lowercase = ''.join(secrets.choice(string.ascii_lowercase) for _ in range(1))
    digit = ''.join(secrets.choice(string.digits) for _ in range(1))
    special_character = ''.join(secrets.choice('!@#$%^&*()_+-=[]{}|\'') for _ in range(1))
    remaining_length = length - 4
    other_characters = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(remaining_length))

    password = uppercase + lowercase + digit + special_character + other_characters
    password = ''.join(random.sample(password, len(password)))  # Shuffle the password

    return password

def create_billing_read_only_policy(policyname_prefix):
    policy_document = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "account:GetAccountInformation",
                    "account:GetAlternateContact",
                    "account:GetContactInformation",
                    "account:ListRegions",
                    "aws-portal:ViewBilling",
                    "billing:GetBillingData",
                    "billing:GetBillingDetails",
                    "billing:GetBillingNotifications",
                    "billing:GetBillingPreferences",
                    "billing:GetCredits",
                    "billing:GetContractInformation",
                    "billing:GetIAMAccessPreference",
                    "billing:GetSellerOfRecord",
                    "billing:ListBillingViews",
                    "ce:ListCostAllocationTags",
                    "ce:Get*",
                    "ce:Describe*",
                    "consolidatedbilling:ListLinkedAccounts",
                    "consolidatedbilling:GetAccountBillingRole",
                    "cur:GetClassicReport",
                    "cur:GetClassicReportPreferences",
                    "cur:GetUsageReport",
                    "cur:DescribeReportDefinitions",
                    "freetier:GetFreeTierAlertPreference",
                    "freetier:GetFreeTierUsage",
                    "invoicing:GetInvoiceEmailDeliveryPreferences",
                    "invoicing:GetInvoicePDF",
                    "invoicing:ListInvoiceSummaries",
                    "organizations:Describe*",
                    "organizations:List*",
                    "payments:GetPaymentInstrument",
                    "payments:GetPaymentStatus",
                    "payments:ListPaymentPreferences",
                    "purchase-orders:GetPurchaseOrder",
                    "purchase-orders:ViewPurchaseOrders",
                    "purchase-orders:ListPurchaseOrderInvoices",
                    "purchase-orders:ListPurchaseOrders",
                    "purchase-orders:ListTagsForResource",
                    "tax:GetTaxRegistrationDocument",
                    "tax:GetTaxInheritance",
                    "tax:ListTaxRegistrations"
                ],
                "Resource": "*"
            }
        ]
    }

    iam_client = boto3.client('iam')
    response = iam_client.create_policy(
        PolicyName=policyname_prefix + generate_random_string(),
        Description='Custom policy for read-only access to billing information',
        PolicyDocument=json.dumps(policy_document)
    )

    return response['Policy']['Arn']

def create_iam_user_with_billing_read_only_access(username, password, arn_of_policy):
    iam_client = boto3.client('iam')
    try:
        response = iam_client.create_user(UserName=username)
        print("User created successfully:", response['User']['UserName'])
    except Exception as e:
        print("Error creating user:", e)
        return
    try:
        response = iam_client.attach_user_policy(
            UserName=username,
            PolicyArn=arn_of_policy
        )
        print("AWSBillingReadOnlyAccess policy attached successfully:", response)
    except Exception as e:
        print("Error attaching policy:", e)
    try:
        response = iam_client.create_login_profile(
            UserName=username,
            Password=password,
            PasswordResetRequired=False
        )
        print("Login profile created successfully:", response)
    except Exception as e:
        print("Error creating login profile:", e)

def delete_users_with_prefix(username_prefix):
    iam_client = boto3.client('iam')
    
    # List all IAM users
    users = iam_client.list_users()['Users']
    for user in users:
        username = user['UserName']
        
        # Check if username starts with the given prefix
        if username.startswith(username_prefix):
            
            # Detach all policies attached to the user
            policies = iam_client.list_attached_user_policies(UserName=username)['AttachedPolicies']
            for policy in policies:
                iam_client.detach_user_policy(UserName=username, PolicyArn=policy['PolicyArn'])
            
            # Delete login profile (console access) if exists
            try:
                iam_client.delete_login_profile(UserName=username)
            except iam_client.exceptions.NoSuchEntityException:
                pass
            
            # Delete the user
            iam_client.delete_user(UserName=username)
            print(f"Deleted user {username}")

def delete_policies_with_prefix(policyname_prefix):
    iam_client = boto3.client('iam')
    
    # List all IAM policies
    policies = iam_client.list_policies(Scope='Local')['Policies'] # Scope='Local' to consider custom policies only
    for policy in policies:
        policy_name = policy['PolicyName']
        
        # Check if policy name starts with the given prefix
        if policy_name.startswith(policyname_prefix):
            # Detach the policy from all users, groups, and roles
            entities = iam_client.list_entities_for_policy(PolicyArn=policy['Arn'])
            
            for user in entities['PolicyUsers']:
                iam_client.detach_user_policy(UserName=user['UserName'], PolicyArn=policy['Arn'])
                
            for group in entities['PolicyGroups']:
                iam_client.detach_group_policy(GroupName=group['GroupName'], PolicyArn=policy['Arn'])
                
            for role in entities['PolicyRoles']:
                iam_client.detach_role_policy(RoleName=role['RoleName'], PolicyArn=policy['Arn'])
            
            # Delete the policy
            iam_client.delete_policy(PolicyArn=policy['Arn'])
            print(f"Deleted policy {policy_name}")


if __name__ == "__main__":
    _31337_effect()

    policyname_prefix = 'BillingReadOnlyAccessCustom_'
    delete_policies_with_prefix(policyname_prefix)
    
    arn_of_policy = create_billing_read_only_policy(policyname_prefix)
    print("arn_of_policy:", arn_of_policy)

    username_prefix = 'read_only_access_to_billing_'
    delete_users_with_prefix(username_prefix)

    username = username_prefix + generate_random_string()
    password = generate_random_password()
    create_iam_user_with_billing_read_only_access(username, password, arn_of_policy)

    sts_client = boto3.client('sts')
    account_id = sts_client.get_caller_identity().get('Account')

    print("AWS Account ID:", account_id)
    print("Username:", username)
    print("Password:", password)
