#!/bin/bash

# Check Official Packages
checkupdates > /tmp/off.updates

# Check AUR Packages
wget -O /tmp/aur.rss https://aur.archlinux.org/rss/
grep "$(pacman -Qm)" /tmp/aur.rss > /tmp/rss.check 
grep "<title>$(pacman -Qm)</title>" /tmp/rss.check > /tmp/aur.updates
