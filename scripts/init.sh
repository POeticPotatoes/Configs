#!/usr/bin/bash


xrandr --output HDMI-0 --pos 0x0 --rotate right --brightness 0.9 --mode 1920x1080 --rate 75 --output DP-0 --primary --pos 1080x420 --rotate normal --mode 1920x1080 --rate 144
nitrogen --restore

