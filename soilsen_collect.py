#!/usr/bin/env python3

import time
import board
from adafruit_seesaw.seesaw import Seesaw
from time import sleep, strftime, time

i2c_bus = board.I2C()

ss = Seesaw(i2c_bus, addr=0x36)
s2 = Seesaw(i2c_bus, addr=0x37)

while True:

	with open ("/home/pi/soildata.csv", "a") as log:

		# read the moisture level through the capacitive touch pad 	
		touch = ss.moisture_read()
		touch2 = s2.moisture_read()

		# read temperature from the temperature sensor
		temp = ss.get_temp()
		temp2 = s2.get_temp()

		# write to the csv file
		log.write("{0}, {1}, {2}, {3}, {4}\n".format(strftime("%Y-%m-%d %H:%M:%S"), str(touch), str(temp), str(touch2), str(temp2)))
		log.close()


		print("Temp1: " + str(temp) + " Moisture1: " + str(touch)+ " Temp2: " + str(temp2) + " Moisture2: " + str(touch2))
		sleep(2)

