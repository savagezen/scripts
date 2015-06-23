#!/bin/zsh
# Check RSS of AUR updates for installed AUR packaces

wget -O /tmp/aur.rss https://aur.archlinux.org/rss/
grep "$(pacman -Qqm)" /tmp/aur.rss > /tmp/rss.check 
grep "<title>$(pacman -Qqm)</title>" /tmp/rss.check > /tmp/aur.updates
