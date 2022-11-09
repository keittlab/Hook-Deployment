#!/usr/bin/env python3

from gpiozero import Button #import button from the Pi GPIO library
import time # import time functions
import os #imports OS library for Shutdown control

shutdownbutton = Button(26) # defines the button as an object and chooses GPIO 26

while True: #infinite loop
        if shutdownbutton.is_pressed: #Check to see if button is pressed
                time.sleep(1) # wait for the hold time we want.
        if shutdownbutton.is_pressed: #check if the user let go of the button
                os.system("sudo shutdown now") #shut down the Pi -h is or -r will reset
        time.sleep(1) # wait to loop again so we don’t use the processor too much.
