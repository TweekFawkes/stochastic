import boto3
import csv

# Initialize an AWS Organizations client
org_client = boto3.client('organizations')

# Recursive function to build the full OU path for a given child ID
def get_ou_path(child_id):
    parents = org_client.list_parents(ChildId=child_id)
    for parent in parents['Parents']:
        if parent['Type'] == 'ORGANIZATIONAL_UNIT':
            ou_info = org_client.describe_organizational_unit(OrganizationalUnitId=parent['Id'])
            ou_name = ou_info['OrganizationalUnit']['Name']
            parent_path = get_ou_path(parent['Id'])
            return f"{parent_path}/{ou_name}" if parent_path else ou_name
    return ""

# Define the CSV file name
csv_file_name = "aws_child_accounts.csv"

# Open the CSV file for writing
with open(csv_file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['Account ID', 'Account Name', 'OU Path'])

    # List accounts in the organization
    paginator = org_client.get_paginator('list_accounts')
    for page in paginator.paginate():
        for account in page['Accounts']:
            account_id = account['Id']
            account_name = account['Name']
            
            # Get the full OU path for the account
            ou_path = get_ou_path(account_id)
            
            # Write the account details to the CSV file
            writer.writerow([account_id, account_name, ou_path])

print(f"{csv_file_name} has been created with the account details.")
