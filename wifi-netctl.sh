#!/bin/sh
# WiFi Connection with Netctl

# Error precautions
rfkill unblock all
ip link set wlp3s0 down
pkill dhcpcd
ip link set wlp3s0 up

# Check Profile
netctl list
echo -n "Is your network listed above? (y/n)  " && read existing
if [[ "$existing" == "y" ]] ; then

	# Use existing profile
	echo -n "Enter Profile (SSID) Name:  " && read profile
	netctl start $profile
else
	# Create new profile
	wifi-menu -o
fi

# only one profile allowed enabled at a time
## sudo netctl  disable [profile]
## sudo netctl switch-to [profile]
