import boto3
import time
from datetime import datetime, timedelta

# Initialize AWS Organizations client
org_client = boto3.client('organizations')

# Initialize Cost Explorer client
ce_client = boto3.client('ce')

# Get the date 72 hours ago
start_date = (datetime.now() - timedelta(hours=72)).strftime('%Y-%m-%d')

# Get today's date
end_date = datetime.now().strftime('%Y-%m-%d')

# A dictionary to store account IDs and their associated costs
account_costs = {}

# List accounts in the organization
paginator = org_client.get_paginator('list_accounts')
for page in paginator.paginate():
    for account in page['Accounts']:
        account_id = account['Id']
        account_name = account['Name']

        # Query the Cost Explorer for the cost of the account over the last 72 hours
        try:
            cost_data = ce_client.get_cost_and_usage(
                TimePeriod={
                    'Start': start_date,
                    'End': end_date
                },
                Granularity='DAILY',
                Filter={
                    'Dimensions': {
                        'Key': 'LINKED_ACCOUNT',
                        'Values': [account_id]
                    }
                },
                Metrics=['UnblendedCost']
            )
        except ce_client.exceptions.LimitExceededException:
            print(f"Rate limit exceeded for account {account_id}. Retrying after a delay...")
            time.sleep(5) # Sleep for 5 seconds
            continue
        
        # Sum the daily costs
        total_cost = sum([float(day['Total']['UnblendedCost']['Amount']) for day in cost_data['ResultsByTime']])
        
        # Store the account ID and total cost
        account_costs[account_id] = {'id': account_id, 'name': account_name, 'cost': total_cost}

# Sort the accounts by cost, in descending order
sorted_accounts = sorted(account_costs.values(), key=lambda x: x['cost'], reverse=True)

# Print the sorted list
for account in sorted_accounts:
    print(f"Account ID: {account['id']}, Account Name: {account['name']}, Cost: ${account['cost']}")
