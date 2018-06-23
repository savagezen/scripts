#!/usr/bin/sh
# bulid kernel for Nexus 6P
# https://forum.xda-developers.com/android/software-hacking/reference-how-to-compile-android-kernel-t3627297

COPPERHEAD_BRANCH=oreo-m3-release
COPPERHEAD_REPO=https://github.com/AndroidHardening/kernel_huawei_angler
BRANCH_KERNEL=oreo-m3-personal

# merge copperheadOS upstream
# $ git checkout $COPPERHEAD_BRANCH
# $ git pull $COPPERHEAD_REPO $COPPERHEAD_BRANCH
# add, commit, and push
# $ git checkout $BRANCH_KERNEL
# $ git merge $COPPERHEAD_BRANCH
# $ git push

LINUX_STABLE_URL=https://github.com/android-linux-stable/angler
LINUX_STABLE_BRANCH=android-msm-angler-3.10

# merge linux-stable
# https://github.com/android-linux-stable/notes
# https://github.com/android-linux-stable/notes/blob/master/trees/angler.md
# $ git checkout linux-stable
# (initial) $ git remote add linux-stable $LINUX_STABLE_URL
# $ git fetch linux-stable $LINUX_STABLE_BRANCH
# $ git merge FETCH_HEAD

# new branches
# new branch: $ git checkout -b new_branch
# copy and create: $ git checkout -b new_branch old_branch
# $ git push origin new_branch

# clean demon files from AK
# wget https://github.com/nathanchance/AnyKernel2/commit/addb6ea860aab14f0ef684f6956d17418f95f29a.diffpatch -p1 < addb6ea860aab14f0ef684f6956d17418f95f29a.diffrm addb6ea860aab14f0ef684f6956d17418f95f29a.diff

# merge AnyKernel2 updates
# $ cd ~/git/anykernel
# $ git checkout master
# $ git pull https://github.com/osm0sis/AnyKernel2.git
# $ git push
# $ git checkout angler-personal
# $ git merge master 
# $ git push

NAME=angler-kernel-$(date +%Y%m%d)
SRC_KERNEL=https://github.com/savagezen/kernel_huawei_angler
SRC_AK=https://github.com/savagezen/anykernel
BRANCH_AK=angler-personal
PREBUILT=https://android.googlesource.com/platform/prebuilts/gcc/linux-x86/aarch64/aarch64-linux-android-4.9
TOOLCHAIN=$(pwd)/prebuilt/bin/aarch64-linux-android-

## pull source ##
git clone $PREBUILT
# or uptedate tools: $ cd ~/git/prebulits; git pull
git clone -b $BRANCH_KERNEL $SRC_KERNEL
git clone -b $BRANCH_AK $SRC_AK

# setup environment
export CROSS_COMPILE=$TOOLCHAIN
export ARCH=arm64
export SUBARCH=arm64

## configure kernel ##
cd kernel_huawei_angler
make clean
make mrproper
make savagezen_defconfig
# make xconfig -> update VERSION string

# build kernel
time make -j2
cp -v arch/arm64/boot/Image.gz-dtb ../anykernel/zImage-dtb
#cp -v arch/arm64/boot/Image.gz-dtb ../aosp_device_huawei_angler-kernel/
cd ../anykernel

# package
zip -r9 $NAME.zip * -x README.md $NAME.zip
