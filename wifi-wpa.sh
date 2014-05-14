#!/bin/sh
# For use with "iw"

iw dev
echo -e "Enter Interface Name:" && read interface

echo "Checking Interface Status..."
iw dev $interface link

echo "Activating Interface..."
ip link set $interface up

echo "Checking that Interface is Up..."
ip link show $interface

echo "Scanning for Access Point..."
iw dev $interface scan| grep SSID

echo -e "Enter Network Name:" && read ssid

echo "Setting ad hoc Network Mode..."
iw dev $interface set type ibss

echo -e "Enter Password for Network ($ssid):"  && read -s psk
touch /etc/wpa_suppliant/$ssid
echo "network={
  ssid=\"$ssid\"
  psk=\"$psk\"
}" > /etc/wpa_supplicant/$ssid

wpa_supplicant -B -i $interface -c /etc/wpa_supplicant/$ssid

dhcpcd $interface