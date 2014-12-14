#!/bin/sh

echo -ne "\n\nOS:			" && cat /etc/*-release | grep "^NAME" | tail -c +6
echo -n "Test Date:		" && date
echo -n "Uptime:		" && uptime -p | tail -c +3
echo -n "Architecture:		" && uname -m
echo -n "Kernel Version:		" && uname -r
echo -n "Installed Packages:	" && ls /var/lib/pacman/local | wc -l
echo -n "Username:		" && whoami
echo -n "Hostname:		" && cat /etc/hostname
echo -n "Shell:			" && echo $SHELL

echo -ne "\nGTK 2 Theme:		" && cat ~/.gtkrc-2.0 | grep gtk-theme | tail -c +18
echo -n "GTK 2 Font Theme:	" && cat ~/.gtkrc-2.0 | grep gtk-font | tail -c +17
echo -n "GTK 2 Icon Theme:	" && cat ~/.gtkrc-2.0 | grep gtk-icon | tail -c +23

echo -ne "\nCPU Model:		" && cat /proc/cpuinfo | grep -m 1 "model name" | tail -c +14
echo -n "CPU Governor:		" && cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
echo -n "I/O Scheduler:		" && cat /sys/block/sd*/queue/scheduler
free -h

echo ""
df -Th -x sys -x tmpfs -x devtmpfs

echo -ne "\nScreen Resolution:	" && xrandr | grep '*' | head -c 12 && echo ""
lspci | grep VGA | grep Intel | tail -c +35
lspci | grep VGA | grep NVIDIA | tail -c +35
lspci | grep VGA | grep AMD | tail -c +35

echo ""
lspci | grep "Network controller" | tail -c +8
lspci | grep Ethernet | tail -c +8
echo -n "External IP Address:	" && curl icanhazip.com
