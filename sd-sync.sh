#!/bin/sh
# Android (Micro)SD Card Media Sync

user=/home/grandtheftjiujitsu
sd=/mnt/sdcard

mount /dev/sdb1 /mnt/sdcard
	# Formatted to Vfat

# Sync Phone Pictures and Video to PC
rsync -rltzuv $sd/DCIM/ $user/Pictures/Phone

# Sync PC Pictures to Phone
rsync -rltzuv --exclude=$user/Pictures/Phone $user/Pictures/ $sd/DCIM/PCpics

# Sync PC Video to Phone
rsync -rltzuv $user/Videos/ $sd/Videos

# Sync PC Music to Phone
rsync -rltzuv $user/Music/ $sd/Music

# NOTE: Permissions ignored - issue writing to Android with aAXv rsync options
