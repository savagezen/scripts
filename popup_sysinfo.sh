#!/bin/zsh
# Clickable Dzen Pop-Up for System Information

USER=$(whoami)
HOST=$(uname -n)
KERNEL=$(uname -r)
BITS=$(uname -m)
SHELL=$(which $SHELL)
MEM=$(free -h | head -n 2)
CPU=$(cat /proc/cpuinfo | grep -m 1 "model name" | tail -c +14 | head -c -11)
CPU_PERC=$(top -b -n1 | grep "Cpu(s)" | awk '{print $2 + $4}')
GOV=$(cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor)
IO=$(cat /sys/block/sda/queue/scheduler)
ENP=$(lspci | grep "Ethernet Controller" | tail -c +62)
GTK_THEME=$(cat ~/.gtkrc-2.0 | grep gtk-theme | tail -c +18)
GTK_FONT=$(cat ~/.gtkrc-2.0 | grep gtk-font | tail -c +17)
GTK_ICON=$(cat ~/.gtkrc-2.0 | grep gtk-icon | tail -c +23)
UPTIME=$( uptime | sed 's/.* up //' | sed 's/[0-9]* us.*//' | sed 's/ day, /d /'\
          | sed 's/ days, /d /' | sed 's/:/h /' | sed 's/ min//'\
            |  sed 's/,/m/' | sed 's/  / /')

(
 # Title
 echo ""
 # The following lines go to slave window
 echo ""
 echo "  $USER @ $HOST for $UPTIME"
 echo ""
 echo " Shell:       $SHELL"
 echo " Kernel:      $KERNEL ($BITS)"
 echo " CPU:         $CPU ($CPU_PERC%)"
 echo " Governor:    $GOV"
 echo " I/O Sched:   $IO"
 echo ""
 echo " $MEM"
 echo ""
 echo "$(df -Th -x sys -x tmpfs -x devtmpfs | tail -n +2)"
 echo ""
 echo " Ethernet Controller:   $ENP"
 echo ""
 echo " GTK2 Theme:            $GTK_THEME"
 echo " GTK2 Font:             $GTK_FONT"
 echo " GTK2 Icon:             $GTK_ICON"
) | dzen2 -p -x "1260" -y "1046" -w "660" -l "20" -sa 'l' -ta 'c'\
    -title-name 'popup_packages' -e 'onstart=uncollapse;button1=exit;button3=exit'

# "onstart=uncollapse" ensures that slave window is visible from start.