#!/bin/bash

echo "Updating Sources"
sudo apt-get update
echo "Installing Build Tools"
sudo apt-get install build-essential python-dev python-smbus python-pip
echo "Installing Python Dependencies"
sudo pip install RPi.GPIO flask flask-classy
git clone https://github.com/adafruit/Adafruit_Python_CharLCD.git
cd Adafruit_Python_CharLCD
sudo python setup.py install
read -p "Reconfiguring Locales. Please enable en_US.utf8. Press [enter] to continue"
sudo dpkg-reconfigure locales

read -p "Select Advanced Options > Enable I2C Driver/Interface > Load at Boot. Press [enter] to continue"
sudo raspi-config