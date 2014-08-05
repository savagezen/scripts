#!/bin/sh

date
echo -n "Uptime:" && uptime | head -c 9

echo -ne "\n\nOS:  " && cat /etc/*-release | grep "^NAME" | tail -c +6
echo -n "Architecture:  " && uname -m
echo -n "Kernel Version:  " && uname -r
echo -n "Installed Packages:  " && ls /var/lib/pacman/local | wc -l

echo -ne "\nUsername:  " && whoami
echo -n "Hostname:  " && cat /etc/hostname
echo -n "Shell:  " && echo $SHELL

echo -ne "\nGTK 2 Theme:  " && cat ~/.gtkrc-2.0 | grep gtk-theme | tail -c +18
echo -n "GTK 2 Font Theme:  " && cat ~/.gtkrc-2.0 | grep gtk-font | tail -c +17
echo -n "GTK 2 Icon Theme:  " && cat ~/.gtkrc-2.0 | grep gtk-icon | tail -c +23

echo -ne "\nCPU Model:  " && cat /proc/cpuinfo | grep -m 1 "model name" | tail -c +14
echo -n "CPU Temp:  " && cat /sys/bus/platform/devices/coretemp.0/temp1_input
echo -n "CPU Governor:  " && cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
echo -n "CPU Usage:  " && top -bn1 | grep "Cpu(s)" | \sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | \awk '{print 100 - $1"%"}'
			# http://stackoverflow.com/questions/9229333/how-to-get-overall-cpu-usage-e-g-57-on-linux
echo -n "I/O Scheduler:  " && cat /sys/block/sd*/queue/scheduler
cat /proc/meminfo | grep MemTotal
cat /proc/meminfo | grep MemFree
cat /proc/meminfo | grep MemAvailable

echo ""
df -Th -x sys -x tmpfs -x devtmpfs		# From alsi.conf

echo -ne "\nScreen Resolution:  " && xrandr | grep '*' | head -c 12 && echo ""
lspci | grep VGA | tail -c +8

echo ""
ip route show
lspci | grep Ethernet | tail -c +8
lspci | grep "Netowrk controller" | tail -c +8

echo -ne "\nPrinter:  " && lpstat -a
