#!/usr/bin/env bash
# https://github.com/xtonousou/xfce4-genmon-scripts

ICON="$HOME/.local/share/icons/xfce4-genmon/cpu/chip.png"
CPU_PERC=$(top -b -n1 | grep "Cpu(s)" | awk '{print $2 + $4}')
CPU_MODEL=$(cat /proc/cpuinfo | grep "model name" | head -n 1 | tail -c +14)
CPU_TEMP_C=$(cat /proc/cpuinfo | grep apicid | head -n 1 | tail -c 3)
CPU_TEMP_F=$((a=$CPU_TEMP_C,b=a/5,c=b*9,d=c+32))
CPU0=$(cat /proc/cpuinfo | grep MHz | head -n 1 | tail -c +12)
CPU1=$(cat /proc/cpuinfo | grep MHz | head -n 2 | tail -n 1 | tail -c +12)
CPU2=$(cat /proc/cpuinfo | grep MHz | tail -n 2 | tail -n 1 | tail -c +12)
CPU3=$(cat /proc/cpuinfo | grep MHz | tail -n 1 | tail -c +12)
GOV=$(cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor)
SCHED=$(cat /sys/block/sda/queue/scheduler)

# Panel
INFO="<img>${ICON}</img>"
INFO+="<txt>"
INFO+="$CPU_PERC% $CPU_TEMP_C ($CPU_TEMP_F 'F)"
INFO+="</txt>"

# Tooltip
MORE_INFO="<tool>"
MORE_INFO+="$CPU_MODEL\n"
MORE_INFO+="CPU0: $CPU0 MHz\n"
MORE_INFO+="CPU1: $CPU1 MHz\n"
MORE_INFO+="CPU2: $CPU2 MHz\n"
MORE_INFO+="CPU3: $CPU3 MHz\n"
MORE_INFO+="Governor: $GOV\n"
MORE_INFO+="Scheduler: $SCHED"
MORE_INFO+="</tool>"

# Panel Print
echo -e "${INFO}"

# Tooltip Print
echo -e "${MORE_INFO}"
