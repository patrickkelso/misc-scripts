#!/usr/bin/python
# Adjust QuickLog to your file path
import pymsgbox 
from datetime import datetime
# Create a file in the same directory as ql.py called ql_vars.py and set 'QLPATH' & 'QuickLog' appropriately. For example:
# QLPATH = "/home/psk/quicklogs"
# QuickLog = QLPATH + "/quick.md"
import ql_vars
response = pymsgbox.prompt('What is on your mind?', title='quick_log')
if type(response) == str:
	currentDT = datetime.now()
	TimeStamp = currentDT.strftime("%Y%m%d%H%M%S")
	HumanTime = currentDT.strftime("%A %B %Y at %-H:%M")
	f = open(ql_vars.QuickLog, "a")
	f.write(TimeStamp + " : " + HumanTime + " : " + response + "\n")
	f.close()
else:
    sys.exit()
