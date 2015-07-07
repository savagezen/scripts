#!/usr/bin/sh
# Update AUR / Git Packages

for AURPKG in $(pacman -Qqm)
do
  cd /tmp
  git clone ssh://aur@aur4.archlinux.org/$AURPKG
  cd $AURPKG
  makepkg -si
  pacman -Qqn ~/abs/pkglist.aur
done
