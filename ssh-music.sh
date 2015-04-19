#!/bin/sh
# Music from Linux to your Mobile Device

# 1) Install and configure an app for your device, such as SSHDroid by Berserker.
# 2) Check your firewall and SSH settings on your host machine.
# 3) Start the SSH client on your device.  Plug it in, this could take a while.
# 4) Check the following items in the command below:
#	- target port (e.g. 22)
#	- host directory (e.g. ~/Music)
#	- target username (e.g. root)
#	- target IP address (e.g. 192.168.1.4)
#	- target directory (e.g. /storage/ext_sd/Music
# 5) Run the script.

rsync -av -e "ssh -p 22" ~/Music/ root@192.168.1.4:/storage/ext_sd/Music
