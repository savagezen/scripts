#!/usr/bin/zsh
# check installed aur versions against update rss

curl https://aur.archlinux.org/rss/ | grep "<title>$(pacman -Qqm)</title>" | sed -e 's/<title>//' | sed -e 's/<\/title>//' | grep "$(pacman -Qqm)" > /tmp/aur.updates
