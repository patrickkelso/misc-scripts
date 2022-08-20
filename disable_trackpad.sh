#!/usr/bin/bash
# I use a Lenovo ThinkPad laptop, and the TouchPoint is all the pointing control I need.
#
# I disable the TrackPad to avoid confusion, and let me rest my wrist on it.
# 
# First identify the trackpad xinput ID
TPAD=$(xinput list |grep "SynPS/2 Synaptics TouchPad" |egrep -o "id=[0-9]+" |egrep -o "[0-9]++")
# Then kill it.
/usr/bin/xinput disable $TPAD
