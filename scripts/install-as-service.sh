#!/bin/bash

set -eu

echo "Installing cabinet-control as service"

sudo cp settings/cabinet-control.service /lib/systemd/system
sudo chmod +x /lib/systemd/system/cabinet-control.service
sudo systemctl daemon-reload
sudo systemctl enable cabinet-control.service
sudo systemctl start cabinet-control.service

echo "Installed 🤘!"
