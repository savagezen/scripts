#!/usr/bin/sh
# AOSP for Nexus 6P

BRANCH=android-8.1.0_r21
BINARY_LINK=https://dl.google.com/dl/android/aosp/huawei-angler-opm3.171019.019-ec4a1fe9.tgz
SOURCE_DIR=aosp
SOURCE=https://android.googlesource.com/platform/manifest

# create build directory
mkdir -p $SOURCE_DIR
cd $SOURCE_DIR

# download source
# git config --global user.name "Your Name"
# git config --global user.email "you@example.com"
repo init -u $SOURCE -b $BRANCH
time repo sync -j4 -c

# setup environment (also in ~/.zshrc)
export USE_CCACHE=1
export CCACHE_DIR=$(pwd)/.ccache
prebuilts/misc/linux-x86/ccache/ccache -M 50G
# make sure Android looks for Java in the right place
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk

# Android expects python2 as 'python'
virtualenv2 venv
. venv/bin/activate

# pull vendor binary
wget $BINARY_LINK
tar -xvf *.tgz
bash extract-huawei-angler.sh
# Enter > ctrl + c, "I ACCEPT"

# clean & prep
make clobber
. build/envsetup.sh
lunch aosp_angler-userdebug

# patch kernel
cp -v ~/git/anykernel/ramdisk/* device/huawei/angler/
# ..> add "import init.savagezen.rc" to device/huawei/angler/init.angler.rc
cp -v ~/git/kernel_huawei_angler/arch/arm64/boot/Image.gz-dtb device/huawei/angler-kernel/

# patch apps / makefile
cp -v ~/git/aosp_build/make/target/product/core.mk build/target/product/core.mk

# patch max fingerprint attempts
sed -i 's/MAX_FAILED_ATTEMPTS_LOCKOUT_PERMANENT\ =\ 20/MAX_FAILED_ATTEMPTS_LOCKOUT_PERMANENT\ =\ 5/' frameworks/base/services/core/java/com/android/server/fingerprint/FingerprintService.java

# patch settings app (temp until git sync)
cp -v ~/git/aosp_packages_apps_Settings/res/xml/device_info_settings.xml packages/apps/Settings/res/xml/
sed -i 's/mPasswordMaxLength\ =\ 16/mPasswordMaxLength\ =\ 64/' packages/apps/Settings/src/com/android/settings/password/ChooseLockPassword.java

# build
time make -j2 otapackage

#cd out/target/product/angler
#adb devices
#adb reboot bootloader
#fastboot devices
#fastboot flash boot boot.img
#fastboot flash system system.img
#fastboot flash vendor vendor.img

#remember
#check TWRP version
#flash gapps
#flash magisk
