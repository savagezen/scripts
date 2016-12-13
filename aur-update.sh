#!/bin/sh

# Creates list of AUR packages, pulls sources, compiles, 
# and installs.  Does not account for dependencies.

PKGLIST=/tmp/aur.pkglist

pacman -Qqm > $PKGLIST

for PKG_NAME in $(cat $PKGLIST)
do
  curl -O https://aur.archlinux.org/cgit/aur.git/snapshot/$PKG_NAME.tar.gz
  tar -xvf $PKG_NAME.tar.gz
  cd $PKG_NAME && makepkg -si
  cd .. && rm -r $PKG_NAME && rm $PKG_NAME.tar.gz
done
