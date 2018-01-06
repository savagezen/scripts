#!/usr/bin/sh
# bulid Savage Kernel for Nexus 6P
# https://github.com/nathanchance/Android-Tools/blob/master/Guides/Building_Flash.txt

FLASH_BRANCH=8.0.0-flash
ANYK_BRANCH=angler-flash-public-8.0.0

FLASH_SOURCE=https://github.com/nathanchance/angler
ANYK_SOURCE=https://github.com/nathanchance/AnyKernel2
PREBUILT_SOURCE=https://android.googlesource.com/platform/prebuilts/gcc/linux-x86/aarch64/aarch64-linux-android-4.9
TOOLCHAIN=$(pwd)/prebuilt/bin/aarch64-linux-android-

# developer clean
#rm -r anykernel
#rm -r flash_kernel

# get source
git clone $FLASH_SOURCE -b $FLASH_BRANCH flash
git clone $ANYK_SOURCE -b $ANYK_BRANCH anykernel
git clone $PREBUILT_SOURCE prebuilt

# setup environment
export CROSS_COMPILE=$TOOLCHAIN
export ARCH=arm64
export SUBARCH=arm64

# add scheduler(s)
cp -v patches/kernel/block/* flash/block/

# add governor(s)
#cp -v patches/kernel/drivers/cpufreq/* flash/drivers/cpufreq/
#cp -v patches/kernel/include/linux/* flash/include/linux/

# configure kernel
cp patches/kernel/arch/arm64/configs/savage_defconfig flash/arch/arm64/conifgs
cd flash
make clean; make mrproper
make savage_defconfig

# build kernel
time make -j4
cp -v arch/arm64/boot/Image.gz-dtb ../anykernel/zImage-dtb
cd ../anykernel

# apply anykernel patches
sed -i -e 's/Flash Kernel by @nathanchance/Savage Kernel by @savagezen/g' anykernel.sh
cp -v ../patches/ak/update-binary META-INF/com/google/android/
cp -v ../patches/ak/init.profiles.sh ramdisk/init.profiles.sh
cat ../patches/ak/init.profiles.rc >> ramdisk/init.profiles.rc

# patch scheduler settings
# battery - noop / 128
# balance / performance - fiops? / 5120
sed -i -e 's/scheduler maple/scheduler noop/g' ramdisk/init.flash.rc
sed -i -e 's/read_ahead_kb 512/read_ahead_kb 5120/g' ramdisk/init.flash.rc

# package
zip -r9 savage_kernel_$(date +%Y%m%d).zip * -x README.md savage_kernel_$(date +%Y%m%d).zip

# developer push
# rm *.zip
# cd flash;  
# cp .config ../savage_defconfig
# cp .config arch/arm64/configs/savage_defconfig; cd ..
# sudo rm -r flash/.git
# sudo rm -r anykernel/.git
# sudo rm -r prebuilt
# git add *
# git commit -m "build: YYYYMMDD"
# git push
