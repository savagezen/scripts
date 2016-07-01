#!/usr/bin/sh
# start internet of things

# start interface
sudo wifi-menu
ping -c 3 www.google.com

# firewall
echo "------------------------"
echo "establishing firewall..."
echo "------------------------"
sudo /home/austin/scripts/iptables.rules

# fetch rootkit scan for conky
echo "running rkhunter..."
echo "-------------------"
sudo rkhunter -c --sk > /tmp/rkhunter

# backup server
echo "starting backup server..."
echo "-------------------------"
systemctl --user start syncthing

# fetch for conky
echo "fetching things for conky..."
echo "----------------------------"
curl -o /tmp/ipinfo ipinfo.io						# ipinfo
cat /tmp/ipinfo | grep postal | tr -d '\"' | tail -c 6 > /tmp/zip	# zip code
checkupdates > /tmp/off.updates						# off pkg updates
