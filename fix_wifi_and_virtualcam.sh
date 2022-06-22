#!/bin/bash

# Written to solve a problem on my Dell Lattitude 5520. 
# Set to autolaunch with i3.

sleep 10
rmmod v4l2loopback
modprobe v4l2loopback devices=1 video_nr=21 exclusive_caps=1 card_label="Virtual Webcam"
rmmod iwlwifi
modprobe iwlwifi
