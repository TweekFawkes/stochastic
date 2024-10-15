#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Print commands and their arguments as they are executed
set -x

# Check if script is run as root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

# Update package information
apt update

# Install prerequisites
apt install -y apt-transport-https ca-certificates curl software-properties-common

# Add Docker's official GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Set up the stable Docker repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update package information again
apt update

# Check Docker versions available
apt-cache policy docker-ce

# Install Docker
apt install -y docker-ce
# apt install -y docker-ce docker-ce-cli containerd.io

# Enable and start Docker service
systemctl enable --now docker

# Verify Docker installation
docker --version
docker ps
docker images
docker run hello-world

# Add current user to docker group to run Docker without sudo (optional)
# usermod -aG docker $SUDO_USER

echo "Docker has been successfully installed and started."
# echo "Please log out and log back in for group changes to take effect."