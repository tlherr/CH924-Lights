#!/bin/bash

echo "Updating Sources"
sudo apt-get update
echo "Installing Build Tools"
sudo apt-get install build-essential python-dev python-smbus python-pip
echo "Installing Python Dependencies"
sudo pip install RPi.GPIO
echo "Reconfiguring Locales. Please enable en_US.utf8"
sudo dpkg-reconfigure locales