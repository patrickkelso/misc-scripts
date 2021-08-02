#!/usr/bin/python
import pymsgbox 
from datetime import datetime
QuickLog = "/home/psk/quick.log"
response = pymsgbox.prompt('What is on your mind?', title='quick_log')
currentDT = datetime.now()
TimeStamp = currentDT.strftime("%Y%m%d%H%M%S")
f = open(QuickLog, "a")
f.write(TimeStamp + " : " + response + "\n")
f.close()
