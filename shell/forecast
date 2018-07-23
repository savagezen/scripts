#!/usr/bin/sh
# for use with dzen2 + conky

ZIP=$(curl ipinfo.io | grep postal | tr -d '\"' | tail -c 6)

(
 # Title
 echo ""
 # Slave
 urxvt -hold -e curl wttr.in/$ZIP
) | dzen -p -title-name 'forecast' -e 'onstart=uncollapse;button1=exit;button3=exit'
