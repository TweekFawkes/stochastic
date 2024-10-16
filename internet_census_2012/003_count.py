import csv
from collections import defaultdict

# Initialize a defaultdict to store port counts
port_counts = defaultdict(int)

# Read the input CSV file
with open('internet_census_2012_tcp_port_open.csv', 'r') as input_file:
    csv_reader = csv.DictReader(input_file)
    
    # Sum up the 'Open' counts for each port
    for row in csv_reader:
        port = int(row['Port'])
        open_count = int(row['Open'])
        port_counts[port] += open_count

# Sort the port_counts by the 'Open' count in descending order
sorted_ports = sorted(port_counts.items(), key=lambda x: x[1], reverse=True)

# Write the consolidated and sorted results to the output CSV file
with open('internet_census_2012_tcp_port_count.csv', 'w', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    
    # Write the header
    csv_writer.writerow(['Port', 'Open'])
    
    # Write the sorted and consolidated data
    for port, open_count in sorted_ports:
        csv_writer.writerow([port, open_count])

print("Processing complete. Results written to 'internet_census_2012_tcp_port_count.csv'")

