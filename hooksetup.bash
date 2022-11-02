#!/bin/bash 
#This File installs and runs all the necesarry commands to set up a fresh Pi with the Hook/Upstream repositories
# run this file with `bash hooksetup.bash`

# Update and Upgrade the RPi to make sure it's up to date
echo "Updating and Upgrading the Pi, this could take a while..."
sudo apt-get update 
sudo apt-get upgrade

# Install needed packages
echo "Installing needed Packages"
sudo apt install pip
sudo apt-get install python3-pip
sudo pip3 install --upgrade setuptools
sudo apt-get install -y i2c-tools
pip3 install python-dateutil
sudo apt -y install at
sudo pip3 install python-dateutil
sudo pip3 install --upgrade adafruit-python-shell
pip install pathlib
sudo apt-get install exfat-fuse
sudo apt-get install exfat-utils

# Installing Sensor Libraries
echo "Installing Sensor Libraries"
pip3 install adafruit-circuitpython-bme280
sudo pip3 install adafruit-circuitpython-seesaw

# Set Up Required Directories
echo "Adding required directories"
bash /home/pi/Hook-Deployment/setup-dirs.bash

# Making Files executable
sudo chmod +x /home/pi/Hook-Deployment/display.py
sudo chmod +x /home/pi/Hook-Deployment/sensor_collect.py

# Installing Python Modules for the MinIO tests
echo "Installing Python Modules for the MinIO tests"
cd upstream-rpi/stengl-minio-tests 
bash minio-clientsetup.bash 

# Setting up the Sunset and Sunrise Recordings
echo "Setting up the Sunrise Sunset Recording Schedule"
rm -rf /home/pi/upstream
ln -s /home/pi/upstream-rpi /home/pi/upstream
mkdir /home/pi/upstream/sound 
sudo cp /home/pi/upstream/crontabs.txt /var/spool/cron/crontabs/pi 
sudo chmod 0600 /var/spool/cron/crontabs/pi 
sudo chown pi /var/spool/cron/crontabs/pi 
sudo systemctl restart cron 
rm /home/pi/upstream-rpi/sunrise-sunset-times.txt
mv /home/pi/Hook-Deployment/sunrise-sunset-times.txt /home/pi/upstream-rpi/sunrise-sunset-times.txt

echo "Scheduling the Recordings..."
bash /home/pi/upstream/upstream-atqcheck.bash 

echo "All done!"




