#!/bin/bash
apt-get update && apt-get install -y awscli python3 python3-pip sudo gcc vim cron git

cd /root
aws s3 cp --recursive s3://setup-files-bucket/setup-files /root

chmod +x /root/unlock.sh

pip3 install ctfcli
pip3 install -r requirements.txt
CTFD_API_KEY=${ctfd_api_key} NUM_PLAYERS=${num_players} python3 -u /root/initialise.py

sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config
systemctl restart sshd
