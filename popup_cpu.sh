#!/usr/bin/zsh
# clickable popup for dzen + conky - cpu info

FG='#008cd5'
BG='#222222'
BITS=$(uname -m)
MEM=$(free -h)
CPU=$(cat /proc/cpuinfo | grep -m 1 "model name" | tail -c +14 | head -c -11)
CPU_PERC=$(top -b -n1 | grep "Cpu(s)" | awk '{print $2 + $4}')
GOV=$(cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor)
IO=$(cat /sys/block/mmcblk0/queue/scheduler)

(
 # Title
 echo " CPU Information"
 # The following lines go to slave window
 echo ""
 echo " $CPU"
 echo ""
 echo " Governor:  $GOV"
 conky -c $HOME/.conky/conkyrc-cpu
) | dzen2 -p '5' -x "1110" -y "19" -w "255" -l "14" -sa 'l' -ta 'c' -fg $FG -bg $BG\
    -title-name 'popup_cpu' -e 'onstart=uncollapse;button1=exit;button3=exit'

# "onstart=uncollapse" ensures that slave window is visible from start
