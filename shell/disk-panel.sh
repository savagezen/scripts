#!/usr/bin/env bash
# https://github.com/xtonousou/xfce4-genmon-scripts

readonly ICON="$HOME/.local/share/icons/xfce4-genmon/disk/database.png"
ROOT_DIR=/dev/mapper/cryptroot
HOME_DIR=/dev/mapper/home-austin
ROOT=$(df -Th $ROOT_DIR | tail -c 6 | head -c 3)
HOME=$(df -Th $HOME_DIR | tail -c 17 | head -c 3)

# Panel
INFO="<img>${ICON}</img>"
INFO+="<txt>"
INFO+="Root: $ROOT Home: $HOME"
INFO+="</txt>"

# Tooltip
MORE_INFO="<tool>"
#MORE_INFO+="┌ $(df -h / | awk '/\/dev/{print $1}' | head -n1)\n"
#MORE_INFO+="├─ Vendor:\t\t$(awk '/[V]endor:/{print $2}' /proc/scsi/scsi)\n"
#MORE_INFO+="├─ Model:\t\t$(awk '/[Mm]odel:/{print $4, $5}' /proc/scsi/scsi)\n"
#MORE_INFO+="├─ Revision:\t\t$(awk '/[Rr]ev:/{print $7}' /proc/scsi/scsi)\n"
#MORE_INFO+="├─ Type:\t\t\t$(awk '/[Tt]ype:/{print $2, $3, $4}' /proc/scsi/scsi)\n"
#MORE_INFO+="└─ Temperature:\t${GET_TEMP} ℃"
MORE_INFO+="$(df -Th -x devtmpfs -x tmpfs)"
MORE_INFO+="</tool>"

# Panel Print
echo -e "${INFO}"

# Tooltip Print
echo -e "${MORE_INFO}"
