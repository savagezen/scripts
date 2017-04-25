#### Building Flash Kernel for Nexus 6P (Angler)

*source:  [Nathan Chancelor's Guilde](https://github.com/nathanchance/Android-Tools/blob/master/Guides/Building_Flash.txt)*

1) Gather Source

```
$ git clone https://github.com/Flash-ROM/kernel_huawei_angler.git flash_kernel
$ git clone https://github.com/Flash-Kernel/AnyKernel2.git anykernel
$ rm -r anykenrel/.git
$ mv anykernel flash_kernel/anykernel
$ cd flash_kernel
```

2) Setup

```
$ git checkout branch-name-7.x.x
$ export PATH=$HOME/android/prebuilts/gcc/linux-86/aarch64/aarch64-linux-android-4.9/bin:$PATH
$ export CROSS_COMPILE=aarch64-linux-android-
$ export ARCH=arm64
$ export SUBARCH=arm64
```

3) Sync and Build

```
$ git reset --hard origin/branch-name

REMOVES FILES NOT FOUND IN SOURCE
$ git clean -f -d -x > /dev/null 2>&1
$ make clean; make mrproper
$ git pull
$ make flahs_defconfig
$ time make -j3
``

4) Make Zip

```
$ mv arch/arm64/boot/Image.gz-dtb anykernel/zImage-dtb
$ cd anykernel

IF ALREADY ZIPPED
$ rm kernel.zip

$ zip -r9 kernel.zip * -x README.md kernel.zip
```
