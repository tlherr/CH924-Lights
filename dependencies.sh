#!/bin/bash

echo "Updating Sources"
sudo apt-get update
echo "Installing Build Tools"
sudo apt-get install build-essential python-dev python-smbus python-pip
echo "Installing Python Dependencies"
sudo pip install RPi.GPIO
git clone https://github.com/adafruit/Adafruit_Python_CharLCD.git
cd Adafruit_Python_CharLCD
sudo python setup.py install
echo "Reconfiguring Locales. Please enable en_US.utf8"
sudo dpkg-reconfigure locales