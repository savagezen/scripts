#!/usr/bin/zsh
# clickable popup for dzen + conky - calendar

FG='#008cd5'
WTTR=$(cat /tmp/forecast | head -n 7 | tail -n 6 | grep F | tail -c 45)

(
 # Title
 echo "$(date +%A,\ %B\ %d)"
 # The following lines go to slave window
 echo ""
 cal | tail -n +2
) | dzen2 -p '5' -x "585" -y "19" -w "200" -l "8" -sa 'c' -ta 'c' -fg $FG\
    -title-name 'popup_cal' -e 'onstart=uncollapse;button1=exit;button3=exit' && sleep 0.1s && transset-df --name popup_cal 0.5

# "onstart=uncollapse" ensures that slave window is visible from start.
