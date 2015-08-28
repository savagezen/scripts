#!/bin/zsh
# Clickable Dzen Pop-Up for Calendar and Weather

FILE=~/.cache/weather.xml

(
 # Title
 echo ""
 # The following lines go to slave window
 echo ""
 echo "  $(date +%R) $(date +%A) $(date +%D)"
 echo ""
 echo "Temp:        $(cat $FILE | grep condition | tail -c 44 | head -c 2)'F"
 echo "Humidity:    $(cat $FILE | grep humidity | head -c 33 | tail -c 2)%"
 echo "  Sunrise:   $(cat $FILE | grep astronomy | head -c 36 | tail -c 7)"
 echo "  Sunset:    $(cat $FILE | grep astronomy | tail -c 11 | head -c 7)"
 echo ""
 echo "$(cal)"
) | dzen2 -p -x "1125" -y "19" -w "240" -l "17" -sa 'c' -ta 'c'\
    -title-name 'popup_cal' -e 'onstart=uncollapse;button1=exit;button3=exit'

# "onstart=uncollapse" ensures that slave window is visible from start.
