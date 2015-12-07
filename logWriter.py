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

	def makeLog(self):
		self.getter.reflesh()
		d = datetime.datetime.today()
		self.lastLog["Brightness"] = self.getter.dataDict["brightness"]
		self.lastLog["Temperature"] = self.getter.dataDict["temp"]
		self.lastLog["Pressure"] = self.getter.dataDict["pressure"]
		self.lastLog["Altitude"] = 45.0
		self.jsonDict["log_"+d.strftime("%H:%M:%S")] = self.lastLog

	def load(self):
		d = datetime.datetime.today()
		today =	"gLog_" + d.strftime("%Y%m%d") + ".json"

		base = os.path.dirname(os.path.abspath(__file__))
		path = os.path.normpath(os.path.join(base, './logs/'+today))
		with open(path, 'r') as f:
			self.jsonDict = json.load(f)
	
	def save(self):
		d = datetime.datetime.today()
		today =	"gLog_" + d.strftime("%Y%m%d") + ".json"

		base = os.path.dirname(os.path.abspath(__file__))
		path = os.path.normpath(os.path.join(base, './logs/'+today))
		
		with open(path, 'w') as f:
			json.dump(self.jsonDict, f, sort_keys=True, indent=4)
