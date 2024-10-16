import csv

input_file = 'internet_census_2012_tcp.csv'
output_file = 'internet_census_2012_tcp_port_open.csv'

# Columns to keep
columns_to_keep = ['Port', 'Open']

with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=columns_to_keep)
    
    # Write header
    writer.writeheader()
    
    # Process each row
    for row in reader:
        # Create a new row with only the desired columns
        filtered_row = {col: row[col] for col in columns_to_keep}
        writer.writerow(filtered_row)

print(f"Processed CSV file has been saved as '{output_file}'")

