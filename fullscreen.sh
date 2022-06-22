#!/bin/bash
# Script to take a full screen screenshot and store it in my NextCloud folder.
# Called by i3 
ncPATH="/home/psk/Documents/nc"
/usr/bin/maim $ncPATH/screenshots/`date +"%Y-%m-%d-%H%M%S"`.png
