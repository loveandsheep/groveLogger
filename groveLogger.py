# -*- coding: utf-8 -*-

import logWriter

log = logWriter.logWriter()

log.init()
log.load()

while True:
	time.sleep(10)
	log.makeLog()
	log.save()