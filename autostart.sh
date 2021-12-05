#!/usr/bin/fish
xrandr --output HDMI1 --auto --right-of eDP1 &
nitrogen --restore &
picom --experimental-backends &
volumeicon &
