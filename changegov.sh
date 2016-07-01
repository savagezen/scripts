#!/bin/zsh
# https://bbs.archlinux.org/viewtopic.php?id=114888

echo -n "Current:  " && cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
echo -n "Change To:  " && read newgov


[[ $(cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor) = $newgov ]] && 
new=$newgov || new=$newgov
echo -n "New: "
echo $new | tee /sys/devices/system/cpu/*/cpufreq/scaling_governor
