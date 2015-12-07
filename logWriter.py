# -*- coding: utf-8 -*-

import groveGetter
import os
import datetime
import locale
import json

class logWriter:
	getter = groveGetter.groveGetter()
	jsonDict = {}
	lastLog = {}

	def init(self):
		self.getter.initialize()
		self.load();

	def makeLog(self):
		self.getter.reflesh()
		d = datetime.datetime.today()
		self.lastLog["Brightness"] = self.getter.dataDict["brightness"]
		self.lastLog["Temperature"] = self.getter.dataDict["temp"]
		self.lastLog["Humidity"] = self.getter.dataDict["humid"]	
		self.lastLog["Pressure"] = self.getter.dataDict["pressure"]
		self.lastLog["Longtitude"] = self.getter.dataDict["Longtitude"]
		self.lastLog["Latitude"] = self.getter.dataDict["Latitude"]
		
		#self.lastLog["Altitude"] = 45.0
		self.jsonDict["log_"+d.strftime("%H:%M:%S")] = self.lastLog
		print "=== Log ===" + d.strftime("%H:%M:%S")
		print "Brightness :" + str(self.lastLog["Brightness"])
		print "Temperature:" + str(self.lastLog["Temperature"])
		print "Humidity   :" + str(self.lastLog["Humidity"])
		print "Pressure   :" + str(self.lastLog["Pressure"])
		print "Latitude   :" + str(self.lastLog["Latitude"])
		print "Longtitude :" + str(self.lastLog["Longtitude"])

	def load(self):
		d = datetime.datetime.today()
		today =	"gLog_" + d.strftime("%Y%m%d") + ".json"

		base = os.path.dirname(os.path.abspath(__file__))
		path = os.path.normpath(os.path.join(base, './logs/'+today))
		if os.path.exists(path):
			with open(path, 'r') as f:
				self.jsonDict = json.load(f)
	
	def save(self):
		d = datetime.datetime.today()
		today =	"gLog_" + d.strftime("%Y%m%d") + ".json"

		base = os.path.dirname(os.path.abspath(__file__))
		path = os.path.normpath(os.path.join(base, './logs/'+today))
		
		with open(path, 'w') as f:
			json.dump(self.jsonDict, f, sort_keys=True, indent=4)
