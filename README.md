# Hook-Deployment
This is the repository for the Hook Sensor Platform Raspberry Pis. 

Set Up:
run these commands 
# make sure the pi is updated
sudo apt-get update 
sudo apt-get upgrade

# install pip
sudo apt-get install python3-pip
sudo pip3 install --upgrade setuptools

# install blinka
cd ~
sudo pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo python3 raspi-blinka.py
# choose yes and yes

# Check i2c
ls /dev/i2c* /dev/spi*
# should see this output
/dev/i2c-1 /dev/spidev0.0 /dev/spidev0.1

# in the Hook Deployment Directory run this command
python3 blinkatest.py

# Install the library for the BME280
pip3 install adafruit-circuitpython-bme280

# Install the Adafruit CircuitPython library for the Soil Moisture Sensor
sudo pip3 install adafruit-circuitpython-seesaw
