import json

class logWriter:
	jsonDict = {}
	lastLog = {}

	def makeLog(self):
		self.lastLog["Temperature"] = 27.0
		self.lastLog["Pressure"] = 1024.0
		self.lastLog["Altitude"] = 45.0
		self.jsonDict["log_14:00"] = self.lastLog

	def load(self):
		today = "gLog_20151201.json"

		with open(today, 'r') as f:
			self.jsonDict = json.load(f)
	
	def save(self):
		today = "gLog_20151201.json"

		with open(today, 'w') as f:
			json.dump(self.jsonDict, f, sort_keys=True, indent=4)
