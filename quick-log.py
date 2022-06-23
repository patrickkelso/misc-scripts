#!/usr/bin/python
# Fast script to capture what I'm doing.
# 
# Create a file in the same directory as quick-log.py called ql_vars.py and set 'QLPATH' & 'QuickLog' appropriately. For example:
# QLPATH = "/home/psk/quicklogs"
# QuickLog = QLPATH + "/quick.md"
#
# Requires pymsgbox 
#
#

import pymsgbox 
from datetime import datetime
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
