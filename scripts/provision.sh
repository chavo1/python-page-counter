#!/usr/bin/env bash

# update db
apt update
# install python redis flask
apt install software-properties-common -y
add-apt-repository ppa:deadsnakes/ppa
apt update
apt install -y python3.7 -y
apt install python3-pip -y
pip3 install -U Flask
pip3 install redis

cat <<EOF > /etc/systemd/system/flask.service
[Unit]
Description=Flask
After=network-online.target

[Service]
Restart=on-failure
WorkingDirectory=/vagrant
ExecStart=/usr/bin/python3 /vagrant/counter.py

[Install]
WantedBy=multi-user.target
EOF
systemctl daemon-reload
systemctl start flask.service

echo Please use to connect to the application: http://`hostname -I | sed -E 's/^\s*\S+\s+(\S+).*/\1/'`:5000
