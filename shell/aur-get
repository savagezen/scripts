#!/usr/bin/sh

# install package from AUR

# pull
cd /tmp
git clone https://aur.archlinux.org/$1.git

# compile
cd $1
makepkg -si

# clean up
#rm -r /tmp/$1*
