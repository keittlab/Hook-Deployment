# Hook-Deployment
This is the repository for the Hook Sensor Platform Raspberry Pis. This Repository is used in unison with the Upstream repository https://github.com/jeaimehp/upstream-rpi.git

# Set Up:
Run these commands on a fresh RPi

# Make sure the pi is updated
```
sudo apt-get update 
sudo apt-get upgrade
```
# Install Packages
```
sudo apt install git
sudo apt install pip
sudo apt-get install python3-pip
sudo pip3 install --upgrade setuptools
sudo apt-get install -y i2c-tools
```
#Enable SSH and i2c
```
sudo raspi-config
```
Select '3 Interface Options' and enable SSH, then repeat and enable I2C
# Set Up the RTC
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
To check the RTC time
```
sudo hwclock -r 
```
Make sure the Timezone is correct
```
sudo raspi-config
```
select "5 Localization Options", then select "L2 Timezone" and select the correct timezone, for Austin select US then Central

# Clone the repositories
Enter these commands from the home directory
```
git clone https://github.com/jeaimehp/upstream-rpi.git
git clone https://github.com/keittlab/Hook-Deployment.git
```
# Run the Setup bash script
```
bash Hook-Deployment/hooksetup.bash
```
# Run the Raspi-Blinka Scripts, enter Y, will reboot the pi
```
sudo python raspi-blinka.py
```
# Check Blinka
```
python3 Hook-Deployment/blinkatest.py
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
# Checking the i2c devices  
Solder the AD0 pad on ONE of the Soil moisture sensors to change the i2c address for one of the soil moisture sensors to 0x37
Enter this command to check the visible devices
```
i2cdetect -y 1
```
Should see this output

![image](https://user-images.githubusercontent.com/45701166/195462601-e89c3723-71dc-4676-90ad-39358cb91333.png)

The BME280 address should be 0x77, The Soil Moisture sensors should be 0x36 and 0x37, the RTC should be 0xUU in cell 0x68, the Display should be 0x3c
# Check that the Microphone is Recording
```
./upstream-rpi/upstream-sound.bash
```
Wait for the recording to finish and check the sound directory in /upstream-rpi to see if there is a recording
```
cd upstream-rpi/sound/
ls
```
There should be a new recoring with the pi's hostname in the directory 
# Set the Soft Shutdown and Display Scripts to run in background on startup
```
sudo nano /etc/rc.local
```
Enter these lines befor the 'exit 0' at the end of the file
```
# Run Soft Shutdown script
sudo python3 /home/pi/Hook-Deployment/softshutdown.py &

# Run Display Script
sudo python3 /home/pi/Hook-Deployment/display.py &
```
# Add the Display Script to Crontab 
```
crontab -e
```
Enter the following lines into crontab
```
# Update Display
* * * * * python3 /home/pi/Hook-Deployment/display.py
```
Enter this line at the top of the file underneath the other reboot commands
```
@reboot python3 /home/pi/Hook-Deployment/softshutdown.py &
```

# Add Environmental Data Collection to Crontab for every 10 min
```
crontab -e
```
Copy and paste this line into the Crontab
```
#Collect Environmental Data
*/10 * * * * /usr/bin/python3 /home/pi/Hook-Deployment/sensor_collect.py >> /DATA/logs/sensors.log
```
CTRL X to exit and then save 
# Add the File Transfer and Clean up to Crontab
```
crontab -e
```
Copy and Paste these lines into the Crontab
```
#Sensor file (csv) transfers
* 12 * * * /home/pi/upstream/stengl-minio-tests/transfersensorfiles.bash >> /DATA/logs/sound-xfer.log

#Sensor file (csv)  clean up
* 13 1-31/2 * * /home/pi/upstream/stengl-minio-tests/cleanup-all-transferedsensorfiles.bash >> /DATA/logs/soundfile-cleanup.log
```
CTRL X to exit and then save

# Setting Up Minio client
```
cd upstream-rpi/stengl-minio-tests/
bash minio-clientsetup.bash
nano .env
```
You will need to use Stache.utexas to get the information to enter into the .env file. Once the information is copied, use CTRL+X to exit and save. Enter this command to test
```
python3 stengl-miniotest.py
```
