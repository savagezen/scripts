#!/usr/bin/zsh
# clickable pop up for dzen + conky - memory information

FG='#008cd5'
(
 # Title
 echo "Memory Information"
 # The following lines go to slave window
 echo ""
 conky -c $HOME/.conky/conkyrc-mem
) | dzen2 -p '5' -x "1110" -y "19" -w "255" -l "13" -sa 'l' -ta 'c' -fg $FG\
    -title-name 'popup_mem' -e 'onstart=uncollapse;button1=exit;button3=exit'

# "onstart=uncollapse" ensures that slave window is visible from start
