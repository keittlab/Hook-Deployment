#!/usr/bin/env python3

# Copyright (c) 2017 Adafruit Industries
# Author: Tony DiCola & James DeVito

import board
import busio
from PIL import Image, ImageDraw, ImageFont
import Adafruit_SSD1306
import digitalio
from time import time, strftime, sleep
import string
import subprocess
from os import path, uname
from adafruit_bme280 import basic as adafruit_bme280

# Raspberry Pi pin configuration:
RST = None

# Create i2c instance
try:
        i2c = busio.I2C(board.SCL, board.SDA)
except:
        print("Couldn't create the i2c instance")

try:
        bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
        # setting location's Pressure (hPa) at Sea level, Austin TX
        bme280.sea_level_pressure = 1019
except:
        print(strftime("%Y-%m-%d-%H:%M:%S") + ": BME280 i2c address could not be found.")

# Add hardware reset pin
#reset_pin = digitalio.DigitalInOut(board.D3) # any pin!

# Create the SSD1306 instance
try:
        disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
except:
        print("Couldn't create the SSD1306 Instance")

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

width = disp.width
height = disp.height

# Define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding

# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (disp.width, disp.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Load default font.
font = ImageFont.load_default()

while True:
        # Draw a black filled box to clear the image.
        draw.rectangle((0,0,width,height), outline=0, fill=0)

        # Shell scripts for system monitoring from here : https://unix.stackexchange.com/questions/1191>        cmd = "hostname -I | cut -d\' \' -f1"
        IP = subprocess.check_output(cmd, shell = True )
        Hostname = uname()[1]
        cmd = "iwgetid"
        try:
                Wifi = subprocess.check_output(cmd, shell = True )
        except:
                Wifi = "No Wifi"
        # Collect BME Data
        try:
                temp = bme280.temperature
                hum = bme280.relative_humidity
        except:
                print(strftime("%Y-%m-%d-%H:%M:%S") + ": Could not collect data from the BME280.")
                temp="n/a"
                hum="n/a"

        # Write Strings to the display
        draw.text((x, top),       "Host Name: " + str(Hostname),  font=font, fill=255)
        draw.text((x, top+8),     "IP: " + str(IP),  font=font, fill=255)
        draw.text((x, top+16),    strftime("%Y-%m-%d:%H:%M:%S"),  font=font, fill=255)
        draw.text((-70, top+25),    str(Wifi),  font=font, fill=255)
        draw.text((x, top+33),    "BME Temp: " + str(temp),  font=font, fill=255)
        draw.text((x, top+41),    "BME Hum: " + str(hum),  font=font, fill=255)
        
        # Display image.
        disp.image(image)
        disp.display()
        sleep(1)
