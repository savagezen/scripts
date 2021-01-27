#!/usr/bin/env bash
# https://github.com/xtonousou/xfce4-genmon-scripts

readonly ICON="$HOME/.local/share/icons//xfce4-genmon/music/spotify.png"
readonly ARTIST=$(cmus-remote -Q | grep "tag artist" | tail -c +12)
readonly TITLE=$(cmus-remote -Q | grep title | tail -c +11)
readonly VOL=$(cmus-remote -Q | grep vol_left | tail -c 3)
readonly SHUFFLE=$(cmus-remote -Q | grep shuffle | tail -c +13)
readonly REPEAT=$(cmus-remote -Q | grep repeat | head -n 1 | tail -c +12)

# Panel
  INFO="<img>$ICON</img>"
  INFO+="<txt>"
  INFO+=" Vol: $VOL% | $ARTIST - $TITLE"
  INFO+="</txt>"

# Tooltip
  MORE_INFO="<tool>"
  MORE_INFO+="Volume: $VOL\n"
  MORE_INFO+="Shuffle: $SHUFFLE\n"
  MORE_INFO+="Repeat: $REPEAT"
  MORE_INFO+="</tool>"

# Panel Print
echo -e "${INFO}"

# Tooltip Print
echo -e "${MORE_INFO}"
