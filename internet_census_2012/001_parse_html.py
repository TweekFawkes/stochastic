import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('Internet_Census_2012-001.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table
table = soup.find('table', id='sortable')

# Open a CSV file to write the data
with open('internet_census_2012.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write the header
    headers = [th.text.strip() for th in table.find_all('th')]
    csv_writer.writerow(headers)
    
    # Write the data rows
    for row in table.find_all('tr')[1:]:  # Skip the header row
        columns = row.find_all('td')
        if columns:
            data = [col.text.strip() for col in columns]
            csv_writer.writerow(data)

print("CSV file 'internet_census_2012.csv' has been created successfully.")

