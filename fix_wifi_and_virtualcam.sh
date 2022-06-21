#!/bin/bash

sleep 10
rmmod v4l2loopback
modprobe v4l2loopback devices=1 video_nr=21 exclusive_caps=1 card_label="Virtual Webcam"\n
rmmod iwlwifi
modprobe iwlwifi
