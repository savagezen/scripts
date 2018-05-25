#!/usr/bin/sh
# android / adb backup to pc

DEST_DIR=$HOME/gdrive_personal/phone_backup/
DEST_DIR2=$HOME/dropbox
PULL=adb pull

# check for connected device
adb devices

# pull system backup stuff
$PULL /boot $DEST_DIR/
$PULL /system $DEST_DIR/
$PULL /vendor $DEST_DIR/
$PULL /data $DEST_DIR/

# reverse with '$adb push $DEST_DIR/* /'

# backup user data
$PULL /sdcard/Download $DEST_DIR/sdcard/
$PULL /sdcard/MagiskManager $DEST_DIR/sdcard/
$PULL /sdcard/Music $DEST_DIR/sdcard/
$PULL /sdcard/Notifications $DEST_DIR/sdcard/
$PULL /sdcard/Playlists $DEST_DIR/sdcard/
$PULL /sdcard/Recordings $DEST_DIR/sdcard/
$PULL /sdcard/Ringtones $DEST_DIR/sdcard/
$PULL /sdcard/Signal $DEST_DIR/sdcard/
$PULL /sdcard/TitaniumBackup $DEST_DIR2/
