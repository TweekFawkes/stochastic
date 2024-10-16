import csv

# Open the CSV file
with open('internet_census_2012_tcp_port_count.csv', 'r') as file:
    reader = csv.DictReader(file)
    existing_ports = set(int(row['Port']) for row in reader)

# Find missing ports
all_ports = set(range(65536))  # 0 to 65535
missing_ports = all_ports - existing_ports

# Append missing ports to the file
with open('internet_census_2012_tcp_port_count.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    for port in missing_ports:
        writer.writerow([port, 0])

print(f"Added {len(missing_ports)} missing ports with count 0.")

