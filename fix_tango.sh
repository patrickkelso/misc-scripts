#!/bin/bash
xdotool keyup Super_L;
sleep 0.1
xdotool key --clearmodifiers BackSpace;
sleep 0.1
xdotool key --clearmodifiers BackSpace;
sleep 0.1
xdotool key --clearmodifiers BackSpace;
sleep 0.1
xdotool key --clearmodifiers Tab;
sleep 0.1
xdotool type "$(xsel)"
