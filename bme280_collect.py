from time import sleep, strftime, time
import board
import csv
from adafruit_bme280 import basic as adafruit_bme280

# creating the sensor object, uses the boards default I2C bus
i2c = board.I2C()
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# setting location's Pressure (hPa) at Sea level, Austin TX
bme280.sea_level_pressure = 1019

# Collecting and writing data to the CSV
with open("/home/anniespi/data.csv", "a") as log:
	while True:
		# creating the data variables
		temp = bme280.temperature
		hum = bme280.relative_humidity
		pres = bme280.pressure
		alt = bme280.altitude
		log.write("{0},{1},{2},{3},{4}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp), str(hum), str(pres),str(alt)))

# Print commands for testing
#		print("\nTemperature: %0.2f C" % bme280.temperature)
#		print("Humidity: %0.2f %%" % bme280.relative_humidity)
#		print("Pressure: %0.2f hPa" % bme280.pressure)
#		print("Altitude: %0.2f meters" % bme280.altitude)

		sleep(2)

