#!/bin/bash

set -eu

echo "Installing cabinet-control as service"

sudo ln -s ./settings/cabinet-control.service /lib/systemd/system/cabinet-control.service
sudo chmod +x /lib/systemd/system/cabinet-control.service
sudo systemctl daemon-reload
sudo systemctl enable cabinet-control.sevice
sudo systemctl start cabinet-control.service

echo "Installed 🤘!"
