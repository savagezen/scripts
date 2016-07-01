#!/usr/bin/zsh
# dzen popup for network information

FG='#008cd5'
FILE=/tmp/ipinfo
EXIP=$(cat $FILE | grep '\"ip\"' | tr -d '\"' | tr -d ',' | tail -c 15)
CITY=$(cat $FILE | grep city | tr -d '\"' | tr -d ',')
STATE=$(cat $FILE | grep region | tr -d '\"' | tr -d ',')
LOC=$(cat $FILE | grep loc | tr -d '\"' | tr -d ',')
ORG=$(cat $FILE | grep '\"org\"' | tr -d '/"')

(
 #Title
 echo "Network Information"
 #The following lines go to slave window
 echo "-------------------"
 conky -c $HOME/.conky/conkyrc-net
 echo "External IP: $EXIP"
 echo ""
 echo "$CITY"
 echo "$STATE"
 echo ""
 echo "$LOC"
 echo "$ORG"
) | dzen2 -p '5' -x "980" -y "19" -w "385" -l "14" -sa 'c' -ta 'c' -fg $FG\
    -title-name 'popup_network' -e 'onstart=uncollapse;button1=exit;button3=exit'

# "onstart=uncollapse" ensures that slave window is visible from start.
