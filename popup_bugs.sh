#!/usr/bin/zsh
# clickable popup for dzen + conky - bugcheck

FG='#008cd5'
LOG=/tmp/rkhunter
F_CHK=$(cat $LOG | grep "Files checked")
F_SUSP=$(cat $LOG | grep "Suspect files")
A_CHK=$(cat $LOG | grep "Applications checked")
A_SUSP=$(cat $LOG | grep "Suspect applications")
RK_CHK=$(cat $LOG | grep "Rootkits checked")
RK_SUSP=$(cat $LOG | grep "Possible rootkits")

(
 # Title
 echo "Rkhunter Results"
 # The following lines go to slave window
 echo "----------------"
 echo "$F_CHK"
 echo "$F_SUSP"
 echo ""
 echo "$RK_CHK"
 echo "$RK_SUSP"
 echo ""
 echo "$A_CHK"
 echo "$A_SUSP"
 echo ""
) | dzen2 -p '5' -x "1125" -y "19" -w "240" -l "10" -sa 'c' -ta 'c' -fg $FG\
    -title-name 'popup_bugs' -e 'onstart=uncollapse;button1=exit;button3=exit'

# "onstart=uncollapse" ensures that slave window is visible from start.
