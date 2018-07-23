#!/usr/bin/sh
# bulid kernel for Nexus 6P
# https://forum.xda-developers.com/android/software-hacking/reference-how-to-compile-android-kernel-t3627297

NAME=angler-kernel-$(date +%Y%m%d)
KERNEL_SOURCE=https://github.com/savagezen/kernel_huawei_angler

AK_SOURCE=https://github.com/savagezen/anykernel
AK_BRANCH=angler-personal

PREBUILT=https://android.googlesource.com/platform/prebuilts/gcc/linux-x86/aarch64/aarch64-linux-android-4.9
TOOLCHAIN=$(pwd)/prebuilts/bin/aarch64-linux-android-

LINUX_STABLE_SOURCE=https://github.com/android-linux-stable/angler
LINUX_STABLE_BRANCH=android-msm-angler-3.10

FK_BRANCH=oreo-mr1
FK_SOURCE=https://github.com/franciscofranco/angler

# pull source
git clone $PREBUILT
git clone $KERNEL_SOURCE -b $FK_BRANCH
git clone $AK_SOURCE -b $AK_BRANCH

# set up environment
export ARCH=arm64
export SUBARCH=arm64
export CROSS_COMPILE=$TOOLCHAIN
cd kernel_huawei_angler

# merge linux-stable
## https://github.com/android-linux-stable/notes
## https://github.com/android-linux-stable/notes/blob/master/trees/angler.md
git fetch $LINUX_STABLE_MERGE $LINUX_STABLE_BRANCH
git merge FETCH_HEAD
## add, commit, push

# merge franco kernel upstream
git fetch $FK_SOURCE $FK_BRANCH
git merge FETCH_HEAD
## add, commit, push

# configure kernel #
make clean
make mrproper
make savagezen_defconfig
## make xconfig -> update VERSION string

# build kernel
time make -j2
## cp -v arch/arm64/boot/Image.gz-dtb ../aosp_device_huawei_angler-kernel/

# package
cd ../anykernel
## clean demon files from AK
## wget https://github.com/nathanchance/AnyKernel2/commit/addb6ea860aab14f0ef684f6956d17418f95f29a.diffpatch -p1 < addb6ea860aab14f0ef684f6956d17418f95f29a.diffrm addb6ea860aab14f0ef684f6956d17418f95f29a.diff
cp -v kernel_huawei_angler/arch/arm64/boot/Image.gz-dtb zImage-dtb
zip -r9 $NAME.zip * -x README.md $NAME.zip
