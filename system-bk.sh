#!/bin/sh
#backup by system configuration

# archive boot
tar -czf /home/austin/gdrive_bk/system/boot.tar.gz /boot

# system configs
tar -czf /home/austin/gdrive_bk/system/etc.tar.gz /etc

# official packages
pacman -Qqe > /home/austin/gdrive_bk/system/off.pkglist

# aur packages
pacman -Qqm > /home/austin/gdrive_bk/system/aur.pkglist


