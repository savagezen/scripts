#!/usr/bin/zsh
# clickable popup for dzen + conky - battery info

FG='#008cd5'
(
 #Title
 echo "Battery Info"
 #The following lines go to slave window
 echo "------------"
 conky -c $HOME/.conky/conkyrc-bat
) | dzen2 -p '5' -x "1165" -y "19" -w "200" -l "5" -sa 'c' -ta 'c' -fg $FG\
    -title-name 'popup_bat' -e 'onstart=uncollapse;button1=exit;button3=exit'

# "onstart=uncollapse" ensures that slave window is visible from start.
