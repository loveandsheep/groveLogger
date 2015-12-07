
from grove_i2c_barometic_sensor_BMP180 import BMP085
import RPi.GPIO as GPIO
import grovepi
import smbus
import time
import math

pins_dht = 4
pins_bright = 14 # Pin 14 is A0 Port.

class groveGetter:
	
	dataDict = {}
	bmp = None
	
	def initialize(self):
		grovepi.pinMode(pins_bright,"INPUT")
		self.bmp = BMP085(0x77, 1)
		rev = GPIO.RPI_REVISION
		if rev == 2 or rev == 3:
			bus = smbus.SMBus(1)
		else:
			bus = smbus.SMBus(0)

	def reflesh(self):
		[temp,humidity] = grovepi.dht(pins_dht,1)
		pressure = self.bmp.readPressure()
		
		self.dataDict["brightness"] = grovepi.analogRead(pins_bright)
		self.dataDict["temp"] = temp
		self.dataDict["humid"] = humidity
		self.dataDict["pressure"] = pressure
