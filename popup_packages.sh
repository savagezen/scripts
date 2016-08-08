#!/bin/zsh
# clickable popup for dzen + conky - package information

FG='#008cd5'
BG='#222222'
PACKAGES=$(pacman -Q | wc -l)
AUR=$(pacman -Qm | wc -l)
OR=$(pacman -Qdt | wc -l)
TP=$(paclist testing | wc -l)
UPDATED=$(awk '/upgraded/ {line=$0;} END { $0=line; gsub(/[\[\]]/,"",$0); \
     printf "%s %s",$1,$2;}' /var/log/pacman.log)
TRANS=$(cat /var/log/pacman.log | grep PACMAN | tail -n 1 | tail -c +37)
AURUP=$(cat /tmp/aur.updates | wc -l)
OFFUP=$(cat /tmp/off.updates | wc -l)

(
 # Title
 echo "Package Information"
 # The following lines go to slave window
 echo ""
 echo "  Last Full Upgrade:   $UPDATED"
 echo "  Last Transaction:   $TRANS"
 echo "  Installed Packages:  $PACKAGES"
 echo "  Unofficial Pkgs:     $AUR"
 echo "  Orphans:             $OR"
 echo "  Testing:             $TP"
 echo "  ------------------------"
 echo "  Off Updates:         $OFFUP"
 echo "  AUR Updates:         $AURUP"
) | dzen2 -p '5' -x "966" -y "19" -w "400" -l "11" -sa 'l' -ta 'c' -fg $FG -bg $BG\
    -title-name 'popup_packages' -e 'onstart=uncollapse;button1=exit;button3=exit'

# "onstart=uncollapse" ensures that slave window is visible from start.
