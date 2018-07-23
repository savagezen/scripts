#!/usr/bin/sh
# populate user tmpfs cache
# for use with ~/git/scripts/tmpfs_cache_bk.sh

# restore from backup
rsync -aAXv $HOME/.cache-bk/ $HOME/.cache
rsync -aAXv $HOME/.chromium-bk/ $HOME/.config/chromium

# create links
ln -sf /tmp/.cache $HOME/.cache
ln -sf /tmp/.chromium $HOME/.config/chromium/Default
