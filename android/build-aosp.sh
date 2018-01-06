#!/usr/bin/sh
# AOSP for Nexus 6P
# Build: OPM1.171019.011

BRANCH=android-8.1.0_r1
BINARY_LINK=https://dl.google.com/dl/android/aosp/huawei-angler-opm1.171019.011-41db8ed5.tgz

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
prebuilts/misc/linux-x86/ccache/ccache -M 25G
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

# clean & build
make clobber
. build/envsetup.sh
lunch aosp_angler-userdebug
time make -j2

# install
echo " "
echo "You can now:"
echo "  $ adb reboot bootloader"
echo "  $ fastboot flash boot boot.img"
echo "  $ fastboot flash system system.img"
echo "  $ fastboot flash vendor vendor.img"
echo " "
echo "Remember to also: "
echo " - flash SuperSU.zip and wipe dalvik / cache"
echo " - flash gapps.zip and wipe dalvik / cache"
echo " - flash vendorfix.zip if needed"
echo " - check TWRP version"

# to do - package
# mount / flash boot, system, vendor
