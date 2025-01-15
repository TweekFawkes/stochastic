#!/bin/bash
set -e  # Exit on error

# Load configuration
CONFIG_FILE="/opt/thor.conf"
if [ ! -f "$CONFIG_FILE" ]; then
    echo "Configuration file not found: $CONFIG_FILE"
    exit 1
fi

# Source the config file
source "$CONFIG_FILE"

# Validate required variables
required_vars=("LOGIN" "PASS" "HOST" "REMOTE_DIR" "LOCAL_DIR" "LOG_DIR")
for var in "${required_vars[@]}"; do
    if [ -z "${!var}" ]; then
        echo "Error: Required variable $var is not set in $CONFIG_FILE"
        exit 1
    fi
done

chmod 600 /opt/thor.conf
chown root:root /opt/thor.conf

# Use variables with new names
login="$LOGIN"
pass="$PASS"
host="$HOST"
remote_dir="$REMOTE_DIR"
local_dir="$LOCAL_DIR"
log_dir="$LOG_DIR"

# Logging function
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$log_dir/$base_name.log"
}

# Setup SSH directory and host key (with proper error handling)
mkdir -p ~/.ssh
chmod 700 ~/.ssh
touch ~/.ssh/known_hosts
ssh-keyscan -H "$host" > ~/.ssh/known_hosts 2>/dev/null || {
    log "Failed to scan host key"
    exit 1
}
chmod 600 ~/.ssh/known_hosts

base_name="$(basename "$0")"
lock_file="/tmp/$base_name.lock"
trap "rm -f $lock_file; log 'Script terminated'" SIGINT SIGTERM

# Check if script is already running
if [ -e "$lock_file" ]; then
    log "Script is already running"
    echo "$base_name is running already."
    exit 1
fi

# Validate directories
if [ ! -d "$local_dir" ]; then
    log "Error: Local directory $local_dir does not exist"
    exit 1
fi

# Create lock file and proceed
touch "$lock_file"
log "Starting transfer"

# Perform LFTP transfer
if ! /usr/local/bin/lftp -p 22 -u "$login","$pass" sftp://"$host" << EOF
set mirror:use-pget-n 5
mirror -c --verbose -P5 --log="$log_dir/$base_name.log" --Remove-source-dirs "$remote_dir" "$local_dir"
quit
EOF
then
    log "LFTP transfer failed"
    rm -f "$lock_file"
    exit 1
fi

# Create dated directory and move files
target_dir="/media/qnap/thor_$(date +"%y%m%d")"
if ! mkdir -p "$target_dir"; then
    log "Failed to create target directory"
    rm -f "$lock_file"
    exit 1
fi

if ! mv "$local_dir"/* "$target_dir"/; then
    log "Failed to move files to target directory"
    rm -f "$lock_file"
    exit 1
fi

log "Transfer completed successfully"
rm -f "$lock_file"
trap - SIGINT SIGTERM
exit 0