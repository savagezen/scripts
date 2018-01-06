#!/usr/bin/sh
# make bootable USB

MIRROR=http://mirror.cs.pitt.edu/archlinux/iso
VERSION=$(date +%Y.%m).01
USB=/dev/sdb

#http://mirror.cs.pitt.edu/archlinux/iso/2017.10.01/
#archlinux-2017.10.01-x86_64.iso

cd /tmp

curl -o archlinux.iso $MIRROR/$VERSION/archlinux-$VERSION-x86_64.iso

dd bs=4M if=archlinux.iso of=$USB status=progress && sync
