
from grove_i2c_barometic_sensor_BMP180 import BMP085
import RPi.GPIO as GPIO
import grovepi
import smbus
import time
import math
import sys
import serial

pins_dht = 4
pins_bright = 14 # Pin 14 is A0 Port.

class groveGetter:
	
	dataDict = {}
	bmp = None
	ser = None
	inp=[]
	GGA=[]
	
	def initialize(self):
		grovepi.pinMode(pins_bright,"INPUT")
		self.ser = serial.Serial('/dev/ttyAMA0', 9600, timeout = 0)
		self.ser.flush()
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

		#GPS
		while True:
			self.inp = self.ser.readline()
			if self.inp[:6] == '$GPGGA'
				break
			time.sleep(0.1)
		try:
			ind=self.inp.index('$GPGGA', 5, len(GPS.inp))
			self.inp = self.inp[ind:]
		expect ValueError:

		self.GGA=self.inp.split(",")
		[t,fix,sats,alt,lat,lat_ns,long,long_ew] = self.GGA.vals()

		lat = g.decimal_degrees(float(lat))
		if lat_ns == "S":
			lat = -lat

		long = g.decimal_degrees(float(long))
		if long_ew == "W"
			long = -long

		self.dataDict["Latitude"] = lat
		self.dataDict["Longtitude"] = long

