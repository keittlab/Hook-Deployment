# Hook-Deployment
This is the repository for the Hook Sensor Platform Raspberry Pis. 

# Set Up:
run these commands 

# Make sure the pi is updated
```
sudo apt-get update 
sudo apt-get upgrade
```

# Install pip
```
sudo apt-get install python3-pip
sudo pip3 install --upgrade setuptools
```

# Install blinka
```
cd ~
sudo pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo python3 raspi-blinka.py
```
choose yes and yes

# Check i2c
```
ls /dev/i2c* /dev/spi*
```
should see this output
```
/dev/i2c-1 /dev/spidev0.0 /dev/spidev0.1
````

# Checking the i2c devices  
Solder the AD0 pad on ONE of the Soil moisture sensors to change the i2c address for one of the soil moisture sensors
Enter this command to check the visible devices
```
i2cdetect -y 1
```
Should see this output /n 
![image](https://user-images.githubusercontent.com/45701166/195462601-e89c3723-71dc-4676-90ad-39358cb91333.png)
The BME280 address should be 0x77, The Soil Moisture sensors should be 0x36 and 0x37, the RTC should be 0xUU in cell 0x68 

# In the Hook Deployment Directory run this command
```
python3 blinkatest.py
```

# Install the library for the BME280
```
pip3 install adafruit-circuitpython-bme280
```

# Install the Adafruit CircuitPython library for the Soil Moisture Sensor
```
sudo pip3 install adafruit-circuitpython-seesaw
```
# Install Python Libraries
```
pip install pathlib

```

# Add support for exFAT SD card on RPi
```
sudo apt-get install exfat-fuse
sudo apt-get install exfat-utils
```

