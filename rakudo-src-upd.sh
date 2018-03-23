#!/usr/bin/sh
#update rakudo-star aur package source

# pull package source
cd ~/abs
git clone ssh://aur.archlinux.org/rakudo-star
cd rakudo-star

# update source
sed -i "s/pkgver=.*/pkgver=$(date +%Y.%m)/" PKGBUILD

# update checksums
updpkgsums
rm *.tar.gz

# update srcinfo
makepkg --printsrcinfo > .SRCINFO

# push
git status
git add PKGBUILD
git add .SRCINFO
git commit -m "update $(date +%Y.%m) source"
git push

# clean up
cd ~
sudo rm -r ~/abs/rakudo-star
