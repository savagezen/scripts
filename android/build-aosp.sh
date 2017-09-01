#!/usr/bin/zsh
# Build AOSP for Nexus 6P (angler)

MANFC=huawei
MODEL=angler
SOURCE=https://android.googlesource.com/platform/manifest
SOURCE_DIR=$HOME/aosp
VENDOR=$(ls $SOURCE_DIR | grep tgz | tail -c +15 | head -n 6)
OTA_FROM=$SOURCE_DIR/build/tools/releasetools/ota_from_target_files
SIGN_APK=$SOURCE_DIR/build/tools/releasetools/sign_target_files_apks
OUT_DIR=$SOURCE_DIR/out/target/product/$MODEL
PKG_DIR=$HOME/git/only_aosp/ota
KEY_CERT=$HOME/.android-certs

# wants
echo -n "Enter Codename Branch: "
read BRANCH
echo -n "Enter Download Link for Vendor Binary: "
read BINARY_LINK

echo ""
echo "############################"
echo "Fetch and Sync Repo...      "
echo "############################"
echo ""

mkdir -p $SOURCE_DIR
cd $SOURCE_DIR
#git config --global user.name "Your Name"
#git config --globl user.email "you@example.com"
repo init -u $SOURCE -b $BRANCH
repo sync -j4 -c

echo ""
echo "############################"
echo "Fetching Vendor...          "
echo "############################"
echo ""

wget $BINARY_LINK
tar -xvf *.tgz
sh extract-$MANFC-$MODEL.sh
# Enter, ctrl + c, "I ACCEPT"

echo ""
echo "#################################"
echo "Setting up build environment...  "
echo "################################"
echo ""

virtualenv2 venv
. venv/bin/activate
make clobber
. build/envsetup.sh
lunch aosp_$MODEL-userdebug

echo ""
echo "############################"
echo "Making Android...           "
echo "############################"
echo ""

make -j2

# make -j2 otapackage
# make -j2 dist
## to SOURCE/out/dist/

#echo ""
#echo "############################"
#echo "Packaging...                "
#echo "############################"
#echo ""

#cp $OUT_DIR/{boot,system,vendor}.img $PKG_DIR/
# cp other files
#zip -r9 $OUT_DIR/AOSP-$MANFC-$MODEL-$VENDOR.zip $PKG_DIR/*

#echo "############################"
#echo "Signing package...         #"
#echo "############################"
#subject='/C=US/ST=California/L=Mountain View/O=Android/OU=Android/CN=Android/emailAddress=android@android.com'
#mkdir -p ~/.android-certs
#for x in releasekey platform shared media; do ./development/tools/make_key ~/.android-certs/$x "$subject"; done
#$SIGN_APK -o -d $KEY_CERT out/dist/aosp_$MODEL-target_files-eng.$USER.zip /tmp/signed.zip
#$OTA_FROM -k $KEY_CERT/platform /tmp/signed.zip /tmp/final-full-ota.zip

#echo ""
#echo "############################"
#echo "Done!                       "
