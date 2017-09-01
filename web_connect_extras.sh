#!/usr/bin/sh
# post web connection utilities

# testing connection
ping -c 3 www.google.com
echo "--------------------"

# firewall
echo "establishing firewall..."
sudo /home/austin/documents/vault/iptables.rules
echo "--------------------"

# fetch for conky
echo "fetching things for conky..."
curl -o /tmp/ipinfo ipinfo.io                                                                   # ip info
curl http://www.ipinfodb.com/index.php | grep postal | tail -c 12 | head -c 5 > /tmp/zip        # zip code
curl -o /tmp/forecast wttr.in/$(cat /tmp/zip)                                                   # forecast / weather
checkupdates > /tmp/off.updates                                                                 # official packages
$HOME/git/scripts/aur-update-check.sh                                                               # aur packages
echo "--------------------"

# gdrive sync
echo "syncing Google Drive..."
rclone sync gdrive_professional:/ $HOME/gdrive/professional/
rclone sync gdrive_personal:/ $HOME/gdrive/personal/
tar -czf $HOME/gdrive/personal/pc_backup/pictures_archive.tar.gz $HOME/pictures/archive
tar -czf $HOME/gdrive/personal/pc_backup/music.tar.gz $HOME/music
tar --exclude={keys,vault} -czf $HOME/gdrive/personal/pc_backup/documents.tar.gz $HOME/documents
tar -czf $HOME/gdrive/personal/pc_backup/system/user-dotfiles.tar.gz $HOME/git/dotfiles
rclone sync $HOME/gdrive/personal/pc_backup/ gdrive_personal:/pc_backup/
echo "--------------------"

# start local backup server
echo "starting local backup server..."
syncthing

