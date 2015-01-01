#!/bin/sh
# Connect to WiFi with iw

iw dev
echo -n "Enter Interface Name: " && read interface

echo "Checking Interface Status..."
iw dev $interface link

echo "Activating Interface..."
ip link set $interface up

echo "Checking that Interface is Up..."
ip link show $interface

echo "Setting ad hoc Network Mode..."
iw dev $interface set type ibss

echo "Scanning for Access Point..."
iw dev $interface scan| grep SSID
echo -n "Enter Network Name: " && read ssid

echo "Existing profiles:"
ls /etc/wpa_supplicant
echo -n "Is the network you want to connect to listed above (y/n): " && read existing_profile

if [[ "$existing_profile" == "y" ]] ; then
	wpa_supplicant -B -i $interface -c /etc/wpa_supplicant/$ssid
else
	echo -n "Enter Password for Network ($ssid): "  && read -s psk
	touch /etc/wpa_suppliant/$ssid
	echo "network={
	  ssid=\"$ssid\"
	  psk=\"$psk\"
	}" > /etc/wpa_supplicant/$ssid
	wpa_supplicant -B -i $interface -c /etc/wpa_supplicant/$ssid
fi	

dhcpcd $interface
ping -c 1 www.google.com
