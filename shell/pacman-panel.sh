#!/usr/bin/env bash
# Dependencies: bash>=3.2, coreutils, file, grep, iputils, pacman, (yaourt or yay or auracle)
# https://github.com/xtonousou/xfce4-genmon-scripts

readonly ICON="$HOME/.local/share/icons/xfce4-genmon/package-manager/pacman.png"

# Calculate updates
# aur-checkupdate script runs every 4 hours through cron
# see $HOME/scripts/aur-checkupdate and $HOME/.config/root.crontab
readonly AUR=$(cat /tmp/aur.update | wc -l)
readonly OFFICIAL=$(checkupdates | wc -l)
readonly ALL=$(( AUR + OFFICIAL ))

# Panel
if [[ $(file -b "${ICON}") =~ PNG|SVG ]]; then
  INFO="<img>${ICON}</img>"
  INFO+="<txt>"
else
  INFO="<txt>"
  INFO+="Icon is missing!"
fi
INFO+="${ALL}"
INFO+="</txt>"

# Tooltip
MORE_INFO="<tool>"
MORE_INFO+="┌ Outdated packages\n"
MORE_INFO+="├─ From official repositories: ${OFFICIAL}\n"
MORE_INFO+="└─ From unofficial repositories: ${AUR}"
MORE_INFO+="</tool>"

# Panel Print
echo -e "${INFO}"

# Tooltip Print
echo -e "${MORE_INFO}"
