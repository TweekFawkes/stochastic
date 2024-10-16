import csv
from datetime import datetime

def generate_commands():
    # Read the CSV file and get all eligible ports
    ports = []
    with open('internet_census_2012_tcp_port_count-001.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if int(row['Open_Count']) > 0 and int(row['Port']) != 25:
                ports.append(row['Port'])

    # Generate the bash script
    with open('run_commands.sh', 'w') as bash_file:
        bash_file.write('#!/bin/bash\n\n')
        bash_file.write('# Generate timestamp\n')
        bash_file.write('TIMESTAMP=$(date +"%Y%m%d%H%M%S")\n\n')
        bash_file.write('# Function to run zmap with dynamic timestamp\n')
        bash_file.write('run_zmap() {\n')
        bash_file.write('    local ports=$1\n')
        bash_file.write('    zmap -B 10M --target-ports=$ports --list-of-ips-file=input_ips.txt \\\n')
        bash_file.write('    --output-file=${TIMESTAMP}___${ports//,/_} \\\n')
        bash_file.write('    --log-directory=/ops/zmap/logs/ \\\n')
        bash_file.write('    --status-updates-file=/ops/zmap/logs/status.txt \\\n')
        bash_file.write('    --blocklist-file=/ops/zmap/blocklist.conf\n')
        bash_file.write('}\n\n')
        bash_file.write('# Run zmap for different port sets\n')

        for i in range(0, len(ports), 3):
            current_ports = ports[i:i+3]
            if len(current_ports) < 3:
                break  # Stop if we don't have a full set of 3 ports

            port_string = ','.join(current_ports)
            bash_file.write(f'run_zmap "{port_string}"\n')
            
            # Add sleep command (except for the last iteration)
            if i + 3 < len(ports):
                bash_file.write('sleep 21m\n\n')

if __name__ == '__main__':
    generate_commands()
