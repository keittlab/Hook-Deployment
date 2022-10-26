 Copyright (c) 2017 Adafruit Industries
# Author: Tony DiCola & James DeVito

import board
import busio
from PIL import Image, ImageDraw, ImageFont
import Adafruit_SSD1306
import digitalio
from time import time, strftime, sleep
import subprocess
from os import path, uname

# Raspberry Pi pin configuration:
RST = None

# Create i2c instance
try:
        i2c = busio.I2C(board.SCL, board.SDA)
except:
        print("Couldn't create the i2c instance")

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

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    # Shell scripts for system monitoring from here : https://unix.stackexchange.com/questions/119126/c>    cmd = "hostname -I | cut -d\' \' -f1"
    IP = subprocess.check_output(cmd, shell = True )
    Hostname = uname()[1]
    cmd = "iwgetid"
    Wifi = subprocess.check_output(cmd, shell = True )

    # Collect BME Data

    # Write two lines of text.

    draw.text((x, top),       "Host Name: " + str(Hostname),  font=font, fill=255)
    draw.text((x, top+8),     "IP: " + str(IP),  font=font, fill=255)
    draw.text((x, top+16),    strftime("%Y-%m-%d:%H:%M:%S"),  font=font, fill=255)
    draw.text((x, top+25),    str(Wifi),  font=font, fill=255)

    # Display image.
    disp.image(image)
    disp.display()
    sleep(1)
