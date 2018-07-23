#!/usr/bin/sh
# sync and backup tmpfs cache
# for use with ~/scripts/tmpfs_cache_restore.sh

# create backups
rsync -aAXv /tmp/.cache/ $HOME/.cache-bk/
rsync -aAXv /tmp/.chromium/ $HOME/.chromium-bk/
