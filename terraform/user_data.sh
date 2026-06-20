#!/bin/bash

# Log everything for debugging
exec > /var/log/user-data.log 2>&1
echo "Started: $(date)"

# Update and install everything
apt update -y
apt install -y python3-pip apache2 git

# Start Apache
systemctl start apache2
systemctl enable apache2

# Install Python libraries
pip3 install psutil boto3

# Clone project repo
cd /home/ubuntu
git clone https://github.com/jnthn-cloud/cloud-engineering-journey.git
chown -R ubuntu:ubuntu cloud-engineering-journey

# Fix Apache permissions
chown ubuntu:ubuntu /var/www/html/index.html 2>/dev/null || true

# Run monitor + dashboard
cd /home/ubuntu/cloud-engineering-journey
sudo -u ubuntu python3 system_monitor.py
sudo -u ubuntu python3 generate_dashboard.py

# Set up cron
echo "0 * * * * /usr/bin/python3 /home/ubuntu/cloud-engineering-journey/system_monitor.py && /usr/bin/python3 /home/ubuntu/cloud-engineering-journey/generate_dashboard.py" | sudo -u ubuntu crontab -

echo "Completed: $(date)"
