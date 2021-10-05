#!/usr/bin/python
# Adjust QuickLog to your file path
import pymsgbox 
from datetime import datetime
QuickLog = "/home/psk/Documents/nc/quick.log"
response = pymsgbox.prompt('What is on your mind?', title='quick_log')
currentDT = datetime.now()
TimeStamp = currentDT.strftime("%Y%m%d%H%M%S")
HumanTime = currentDT.strftime("%A %B %Y at %-H:%M")
f = open(QuickLog, "a")
f.write(TimeStamp + " : " + HumanTime + " : " + response + "\n")
f.close()
