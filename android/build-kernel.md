#### Building Flash Kernel for Nexus 6P (Angler)

*source:  [Nathan Chancelor's Guilde](https://github.com/nathanchance/Android-Tools/blob/master/Guides/Building_Flash.txt)*

1) Gather Source

~~~
$ git clone https://github.com/Flash-Kernel/AnyKernel2.git anykernel
$ git clone https://github.com/Flash-ROM/kernel_huawei_angler.git flash-kernel
~~~

2) Make the Kernel

#### First Build or New Android Version

* removes files not in repo

~~~
$ cd flash-kernel
$ git checkout <flash-kernel branch>
  e.g. n7.1.2-flash
$ git reset --hard origin/<flash-kernel branch>
  e.g. n7.1.2-flash
$ git clean -f -d -x > /dev/nulll
$ make clean; make mrproper
$ git pull
$ export CROSS_COMPILE=$HOME/android/prebuilts/gcc/linux-x86/aarch64/aarch-64-linux-android-4.9/bin/aarch64-linux-android-
$ export ARCH=arm65
$ export SUBARCH=arm64
$ make flash_defconfig
$ time make -j3
~~~

#### Every Build (after first)

~~~
$ export CROSS_COMPILE=$HOME/android/prebuilts/gcc/linux-x86/aarch64/aarch-64-linux-android-4.9/bin/aarch64-linux-android-
$ export ARCH=arm65
$ export SUBARCH=arm64
$ cp arch/arm64/configs/last_config .config
$ time make -j3
~~~

3) Make Flashable Zip

#### First Build or New Android Version

* removes files not in repo

~~~
$ cd anykernel
$ git checkout angler-flash-public-7.1.X
  -- or angler-flash-release-7.1.X
$ git reset --hard origin/angler-flash-public-7.1.X
$ git clean -f -d -x > /dev/null
$ git pull
$ cp ../flash-kernel/arch/arm64/boot/Image.gz-dtb zImage-dtb
$ zip -r9 kernel.zip * -x README.md kernel.zip
~~~

#### Every Build (after first)

~~~
$ cp ../flash-kernel/arch/arm64/boot/Image.gz-dtb zImage-dtb
$ zip -r9 kernel.zip * -x README.md kernel.zip
~~~

4) (optional) Sync to Personal Repo

~~~
(assumes kernel_huawei_angler is an existing repo on your GitHub)

$ cd ~/git/flash-kernel
$ mv .config arch/arm64/config/last_config
$ make clean; make mrproper

$ cd ..
$ cp kernel_huawei_angler/README.md flash-kernel/
$ cp -r kernel_huawei_angler/.git dot-git-bk
$ rsync -aAXv flash-kernel/ kernel_huawei_angler/
$ rm -r kernel_huawei_angler/.git
$ mv dot-git-bk kernel_huawei_angler/.git

$ mkdir kernel_huawei_angler/anykernel
$ rsync -aAXv anykernel/ kernel_huawei_angler/anykernel
$ rm -r kernel_huawei_angler/anykernel/.git
~~~
