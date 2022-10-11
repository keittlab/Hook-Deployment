import time
import board
from adafruit_seesaw.seesaw import Seesaw
from time import sleep, strftime, time

i2c_bus = board.I2C()

ss = Seesaw(i2c_bus, addr=0x36)

with open ("/home/pi/soildata.csv", "a") as log:


	while True:
		# read the moisture level through the capacitive touch pad 	
		touch = ss.moisture_read()
		# read temperature from the temperature sensor
		temp = ss.get_temp()
		log.write("{0},{1},{2}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(touch),str(temp)))
		
#		print("Tenp: " + str(temp) + " Moisture: " + str(touch))
		sleep(2)

