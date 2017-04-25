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
rclone sync $HOME/pictures/archive/ remote:pc_backup/archive_pics/
rclone sync $HOME/music/ remote:pc_backup/music/
rsync -aAXv --exclude={keys,vault} $HOME/documents/ /tmp/documents
rclone sync /tmp/documents/ remote:pc_backup/local_docs
rm -r /tmp/documents

# start local backup server
echo "starting local backup server..."
syncthing

