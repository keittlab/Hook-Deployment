# Hook-Deployment
This is the repository for the Hook Sensor Platform Raspberry Pis. This Repository is used in unison with the Upstream repository https://github.com/jeaimehp/upstream-rpi.git

# Set Up:
Run these commands on a fresh RPi

# Make sure the pi is updated
```
sudo apt-get update 
sudo apt-get upgrade
```

# Install pip
```
sudo apt install git
sudo apt install pip
sudo apt-get install python3-pip
sudo pip3 install --upgrade setuptools
```
# Clone the repositories
Enter these commands from the home directory
```
git clone https://github.com/jeaimehp/upstream-rpi.git
git clone https://github.com/keittlab/Hook-Deployment.git
```
# Install Python Modules for minio tests
```
cd upstream-rpi/stengl-minio-tests 
bash minio-clientsetup.bash 
```
# Set up the Sunset/Sunrise Recordings
``` 
pip3 install python-dateutil –upgrade 
sudo apt -y install at
sudo pip3 install python-dateutil
rm -rf /home/pi/upstream
ln -s /home/pi/upstream-rpi upstream
mkdir /home/pi/upstream/sound 
sudo cp /home/pi/upstream/crontabs.txt /var/spool/cron/crontabs/pi 
sudo chmod 0600 /var/spool/cron/crontabs/pi 
sudo chown pi /var/spool/cron/crontabs/pi 
sudo systemctl restart cron 
cd /home/pi/upstream-rpi 
rm sunrise-sunset-times.txt 
mv /Hook-Deployment/sunrise-sunset-times.txt /upstream-rpi/sunrise-sunset-times.txt
```
Schedule the Recordings
```
bash /home/pi/upstream/upstream-atqcheck.bash 
```
Check that there is now a recording scheduled for the next sunrise or sunset
```
atq
```
Output should look something like this 
```
1     Tue Oct 25 07:06:00 2022 a pi
```
# Install blinka
```
cd ~
sudo pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo python3 raspi-blinka.py
```
choose yes and yes, the system should Reboot
# Test Blinka
```
cd Hook-Deployment/
python3 blinkatest.py
```
Verify that everything works

# RTC Set Up
```
sudo nano /boot/config.txt
```
Add line below to the end of the file
```
dtoverlay=i2c-rtc,ds3231
```
Then do a reboot
```
sudo reboot
```
Check for the device in i2c, 
Should see UU at 0x68
```
sudo i2cdetect -y 1
```
Disable the Fake Clock
```
sudo apt-get -y remove fake-hwclock
sudo update-rc.d -f fake-hwclock remove
sudo systemctl disable fake-hwclock
sudo nano /lib/udev/hwclock-set
```
Comment out these lines with a #
```
#if [-e /run/systemd/system]; then
#exit 0
#fi
#/sbin/hwclock --rtc=$dev -systz
```
Check the rtc time
```
sudo hwclock -D -r
```
To set the RTC time 
```
sudo hwclock -w 
```
To check the RTC time
```
sudo hwclock -r 
```
# Configure the Soft Shutdown button
``` 
sudo nano /boot/config.txt
```
Add this line to the end of the file with the pin number, in this case 27
```
dtoverylay=gpio-shutdown,gpio_pin=27,active_low=1,gpio_pull=up
```
Exit and save the file then reboot
```
sudo reboot
```

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
Should see this output

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

