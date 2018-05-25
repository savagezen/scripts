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

# create pc backup
echo "Creating PC Backup..."
pacman -Qqm > $HOME/mega/pc_backup/system/aur.pkglist
pacman -Qe > $HOME/mega/pc_backup/system/off.pkglist
tar -czf $HOME/mega/pc_backup/system/etc.tar.gz /etc
tar -czf $HOME/mega/pc_backup/system/boot.tar.gz /boot
tar --exclude={keys,vault} -czf $HOME/mega/pc_backup/$HOME/documents.tar.gz $HOME/documents
echo "--------------------"

# push to backups to Mega
echo "Pushing PC and Phone Backups to Mega..."
rclone sync $HOME/mega/pc_backup/ mega:/pc_backup/
rclone sync $HOME/mega/phone_backup/ mega:/phone_backup/
echo "--------------------"

# pulling from Google Drive
echo "Pulling  Google Drive ..."
rclone sync gdrive_professional:/ $HOME/gdrive_professional/
rclone sync gdrive_personal:/ $HOME/gdrive_personal/
echo "--------------------"

# start local backup server
echo "Starting Syncthing Daemon..."
systemctl start syncthing@austin.service
