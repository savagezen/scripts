#!/usr/bin/sh
# bulid kernel for Nexus 6P
# https://forum.xda-developers.com/android/software-hacking/reference-how-to-compile-android-kernel-t3627297

# merge copperheadOS upstream into fork
BRANCH_UPS=oreo-m3-release
ORIGINAL_OWNER=copperheados
ORIGINAL_REPO=kernel_huawei_angler
# $ git checkout $BRANCH_UPS
# $ git pull https://github.com/$ORIGINAL_OWNER/$ORIGINAL_REPO.git $BRANCH_UPS
# add, commit, and push (to origin/$BRANCH_UPS)

# merge AnyKernel2 updates
# $ cd ~/git/anykernel
# $ git checkout master
# $ git pull https://github.com/osm0sis/AnyKernel2.git
# $ git push
# $ git checkout angler-personal
# $ git merge master 

BRANCH_KERNEL=oreo-m3-personal
BRANCH_AK=angler-personal
SRC_PREBUILT=https://github.com/savagezen/aosp_prebuilts
SRC_KERNEL=https://github.com/savagezen/kernel_huawei_angler
#SRC_KERNEL=https://android.googlesource.com/kernel/msm
SRC_AK=https://github.com/savagezen/anykernel
TOOLCHAIN=$(pwd)/aosp_prebuilts/bin/aarch64-linux-android-

## pull source ##
git clone $SRC_PREBUILT
git clone -b $BRANCH_KERNEL $SRC_KERNEL
git clone -b $BRANCH_AK $SRC_AK

# to copy and create new branch
# $ git checkout -b new_branch old_branch
# $ git push origin new_branch

# setup environment
export CROSS_COMPILE=$TOOLCHAIN
export ARCH=arm64
export SUBARCH=arm64

## configure kernel ##
cd kernel_huawei_angler
make clean
make mrproper
make savagezen_defconfig
#make angler_defconfig

# build kernel
time make -j2
cp -v arch/arm64/boot/Image.gz-dtb ../anykernel/zImage-dtb
cd ../anykernel

# package
zip -r9 kernel_$(date +%Y%m%d).zip * -x README.md kernel_$(date +%Y%m%d).zip
