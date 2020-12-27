#!/usr/bin/env bash
# Dependencies: bash>=3.2, coreutils, file, gawk
# https://github.com/xtonousou/xfce4-genmon-scripts

ICON="$HOME/.local/share/icons/xfce4-genmon/memory/memory.png"

# Calculate RAM values
TOTAL=$(free -b | awk '/^[Mm]em/{$2 = $2 / 1073741824; printf "%.2f", $2}')
USED=$(free -b | awk '/^[Mm]em/{$3 = $3 / 1073741824; printf "%.2f", $3}')
readonly FREE=$(free -b | awk '/^[Mm]em/{$4 = $4 / 1073741824; printf "%.2f", $4}')
readonly SHARED=$(free -b | awk '/^[Mm]em/{$5 = $5 / 1073741824; printf "%.2f", $5}')
readonly CACHED=$(free -b | awk '/^[Mm]em/{$6 = $6 / 1073741824; printf "%.2f", $6}')
readonly AVAILABLE=$(free -b | awk '/^[Mm]em/{$7 = $7 / 1073741824; printf "%.2f", $7}')

# Swap Values
readonly SWP_TOTAL=$(free -b | awk '/^[Ss]wap/{$2 = $2 / 1073741824; printf "%.2f", $2}')
readonly SWP_USED=$(free -b | awk '/^[Ss]wap/{$3 = $3 / 1073741824; printf "%.2f", $3}')
readonly SWP_FREE=$(free -b | awk '/^[Ss]wap/{$4 = $4 / 1073741824; printf "%.2f", $4}')

# Panel
INFO="<img>$ICON</img>"
INFO+="<txt>"
INFO+="$USED / $TOTAL GiB"
INFO+="</txt>"

# Tooltip
MORE_INFO="<tool>"
MORE_INFO+="┌ RAM\n"
MORE_INFO+="├─ Used\t\t${USED} GB\n"
MORE_INFO+="├─ Free\t\t${FREE} GB\n"
MORE_INFO+="├─ Shared\t${SHARED} GB\n"
MORE_INFO+="├─ Cache\t${CACHED} GB\n"
MORE_INFO+="└─ Total\t\t${TOTAL} GB"
MORE_INFO+="\n\n"
MORE_INFO+="┌ SWAP\n"
MORE_INFO+="├─ Used\t\t${SWP_USED} GB\n"
MORE_INFO+="├─ Free\t\t${SWP_FREE} GB\n"
MORE_INFO+="└─ Total\t\t${SWP_TOTAL} GB"
MORE_INFO+="</tool>"

# Panel Print
echo -e "${INFO}"

# Tooltip Print
echo -e "${MORE_INFO}"
