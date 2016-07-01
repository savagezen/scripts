#!/bin/zsh
# Clickable Dzen Pop-Up for Multimedia Information

FG='cyan'
AUDIO=$(amixer get Master)
RES=$(xrandr | grep "*" | head -c 15)
VID=$(lspci | grep VGA | grep NVIDIA | tail -c +35 && lspci | grep VGA | grep Intel | tail -c +35 && lspci | grep VGA | grep AMD | tail -c +35)

(
 # Title
 echo ""
 # The following lines go to slave window
 echo ""
 echo " $(amixer get Master)"
 echo ""
 echo " Screen Resolution:     $RES"
 echo " Video Controller:      $VID"

) | dzen2 -p -x "596" -y "19" -w "770" -l "15" -sa 'l' -ta 'c' -fg $FG\
    -title-name 'popup_packages' -e 'onstart=uncollapse;button1=exit;button3=exit'

# "onstart=uncollapse" ensures that slave window is visible from start.
