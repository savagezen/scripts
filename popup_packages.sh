#!/bin/zsh
# Clickable Dzen Pop-Up for Package Information

PACKAGES=$(pacman -Q | wc -l)
AUR=$(pacman -Qm | wc -l)
OR=$(pacman -Qdt | wc -l)
TP=$(paclist testing | wc -l)
UPDATED=$(awk '/upgraded/ {line=$0;} END { $0=line; gsub(/[\[\]]/,"",$0); \
          printf "%s %s",$1,$2;}' /var/log/pacman.log)
TRANS=$(cat /var/log/pacman.log | grep PACMAN | tail -n 1 | tail -c +37)

(
 # Title
 echo ""
 # The following lines go to slave window
 echo ""
 echo " Installed Packages:  $PACKAGES"
 echo " Unofficial Pkgs:     $AUR"
 echo " Orphans:             $OR"
 echo " Testing:             $TP"
 echo " Last System Upgrade: $UPDATED"
 echo " Last Transaction:    $TRANS"
) | dzen2 -p -x "866" -y "19" -w "500" -l "8" -sa 'l' -ta 'c'\
    -title-name 'popup_packages' -e 'onstart=uncollapse;button1=exit;button3=exit'

# "onstart=uncollapse" ensures that slave window is visible from start.
