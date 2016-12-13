#!/usr/bin/sh

# install package from AUR

# pull
curl -o /tmp/$1.tar.gz https://aur.archlinux.org/cgit/aur.git/snapshot/$1.tar.gz

# extract
cd /tmp && tar -xvf $1.tar.gz

# compile
cd $1 && makepkg -si

# clean up
rm -r /tmp/$1*
