#!/usr/bin/sh
# helper script for building kernel
# reference: https://forum.xda-developers.com/nexus-6p/development/reference-stock-kernel-upstream-linux-t3474540

VERSION=7.1.2
TOOLCHAIN=$HOME/aosp/prebuilts/gcc/linux-x86/aarch64/aarch64-linux-android-4.9/bin/aarch64-linux-android-
SOURCE=$HOME/git/aflash_kernel
UPSTREAM=https://github.com/nathanchance/angler.git $VERSION-flash
ANYK=$HOME/git/anykernel

## gather source
#git clone https://github.com/nathanchance/angler.git source
#git clone https://github.com/nathanchance/AnyKernel2.git anykernel
## clean repo, check branch, pull changes
#cd source; git clean -fxd
#git checkout $VERSION-flash; git pull
#cd ../anykernel; git clean -fxd
#git checkout angler-flash-public-$VERSION; git pull

## setup environment
export CROSS_COMPILE=$TOOLCHAIN
export ARCH=arm64
export SUBARCH=arm64

## merge upstream to fork
cd $SOURCE; git checkout $VERSION-flash
git pull $UPSTREAM
git add *
git commit -m "pull from upstream"
git push
## merge fork 
git checkout $VERSION-aflash
git merge $VERSION-flash
# may need to resolve conflicts
git add *
git commit -m "merge $VERSION-flash to $VERSION-aflash"
git commit

## configure kernel
make clean; make mrproper
make aflash_defconfig

## build kernel
make -j4

## package
cd $ANYK; git checkout angler-aflash-public-$VERSION
cp -v $SOURCE/arch/arm64/boot/Image.gz-dtb $ANYK/zImage-dtb
zip -r9 aFlash_Kernel_$(date +%F).zip * -x README.md aFlash_Kernel_$(date +%F).zip
