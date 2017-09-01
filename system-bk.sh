#!/bin/sh
# backup by system configuration

HOME=/home/austin

# archive boot
tar -czf $HOME/gdrive/personal/pc_backup/system/boot.tar.gz /boot

# system configs
tar -czf $HOME/gdrive/personal/pc_backup/system/etc.tar.gz /etc

# official packages
pacman -Qqe > $HOME/gdrive/personal/pc_backup/system/off.pkglist

# aur packages
pacman -Qqm > $HOME/gdrive/personal/pc_backup/system/aur.pkglist

# change ownership
chown -R austin $HOME/gdrive
