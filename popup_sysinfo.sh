#!/usr/bin/zsh
# Clickable Dzen Pop-Up for System Information

FG='#008cd5'
ICONS=$HOME/.icons/dzen2
USER=$(whoami)
HOST=$(uname -n)
KERNEL=$(uname -r)
BITS=$(uname -m)
SHELL=$(which $SHELL)
UPTIME=$( uptime | sed 's/.* up //' | sed 's/[0-9]* us.*//' | sed 's/ day, /d /'\
          | sed 's/ days, /d /' | sed 's/:/h /' | sed 's/ min//'\
            |  sed 's/,/m/' | sed 's/  / /')

(
 # Title
 echo "System Information"
 # The following lines go to slave window
 echo ""
 echo "  ^i($ICONS/term.xbm)  $SHELL"
 echo "  ^i($ICONS/arch_10x10.xbm)  $KERNEL ($BITS)"
 echo ""
 conky -c $HOME/.conky/conkyrc-sys
) | dzen2 -p '5' -x "1095" -y "19" -w "270" -l "10" -sa 'l' -ta 'c' -fg $FG\
    -title-name 'popup_sysinfo' -e 'onstart=uncollapse;button1=exit;button3=exit'

# "onstart=uncollapse" ensures that slave window is visible from start
