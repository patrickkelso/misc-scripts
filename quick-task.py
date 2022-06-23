#!/usr/bin/python
# Fast script to capture a task.
# The task is captured in a format that Obsidian.md will recognise.
# 
# Requires pymsgbox 
# Create a file in the same directory as quick-task.py called ql_vars.py and set 'QuickTaskPath' appropriately. For example:
# QuickTaskPATH = "/home/psk/quicktasks"
#
#
import pymsgbox 
from datetime import datetime
import ql_vars
currentDT = datetime.now()
TimeStamp = currentDT.strftime("%Y%m%d%H%M%S")
QuickTask = ql_vars.QuickTaskPATH + "/" + TimeStamp + ".md"
response = pymsgbox.prompt('What do you need to do?', title='quick_task')
if type(response) == str:
    f = open(QuickTask, "a")
    f.write("#todo\n" + "- [ ] " + response + "\n")
    f.close()
else:
    sys.exit()
