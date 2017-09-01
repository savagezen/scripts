#### Building AOSP From Source (Nexus 6P - Angler)
---

**1) Gathering Source (45 min)**

See latest [code name releases ](https://source.android.com/source/build-numbers#source-code-tags-and-builds) that correspond to repo branch.

~~~
$ mkdir android
$ cd android

$ git config --global user.name "Your Name"
$ git config --global user.email "you@example.com"

$ repo init -u https://android.googlesource.com/platform/manifest -b CODENAME_BRANCH
$ repo sync -j4 -c
~~~

**2) Proprietary Binaries**

Download [vendor image](https://developers.google.com/android/drivers#angler) that matches the ```Build``` of the above repo branch, then:

~~~
$ tar -xvf huawei-angler-VENORNUMBER-BUILDNUMBER.tgz
$ sh extract-huawei-angler.sh

NOTE - Press 'Enter' to view license, once viewing press CTL + C to skip to agreement.
~~~

**3) Preparation**

~~~
NOTE - Android expects 'python' to be 'python2'

$ virtualenv2 venv
$ . venv/bin/activate

NOTE - Make sure Android looks for Java in the right place
$ export JAVA_HOME=/usr/lib/jvm/java-x-openjdk

$ make clobber
$ . build/envsetup.sh
$ lunch aosp_angler-userdebug
~~~

**4) Customization**

**5) Build (100 min)**

~~~
$ time make -j2

~~~

**6a) Zip Installation (95+ min)**

~~~
$ cd ~/aosp
$ mkdir dist_output
$ make dist DIST_DIR=dist_output
$ ./build/tools/releasetools/ota_from_target_files dist_output/aosp_angler-target_files-eng.austin.zip ota_update.zip

$ subject='/C=US/ST=California/L=Mountain View/O=Android/OU=Android/CN=Android/emailAddress=android@android.com'
$ mkdir ~/.android-certs
$ for x in releasekey platform shared media; do ./development/tools/make_key ~/.android-certs/$x "$subject"; done

$ make dist
$ ./build/tools/releasetools/sign_target_files_apks -o -d ~/.android-certs out/dist/*-target_files-*.zip signed-target_files.zip
$ ./build/tools/releasetools/ota_from_target_files -k ~/.android-certs/releasekey signed-target_files.zip signed-ota_update.zip
~~~

**6b) Manual Installation**

- Backup Your Data! I suggest [SMS Backup +](https://play.google.com/store/apps/details?id=com.zegoggles.smssync) for messages and [Titanium 
Backup](https://play.google.com/store/apps/details?id=com.keramidas.TitaniumBackup) for app / data.
- TWRP backup: ```Boot```, ```System```, ```Vendor```, ```Data```
- TWRP wipe: ```Dalvik / ART Cache```, ```System```, ```Data```, ```Cache```
- Hold ```Power Button``` and ```Volume Down``` until you're booted to the ```Bootloader```
- Connect via USB and check connection with ```$ fastboot devices```, then:
  - ```$ cd out/target/product/angler```
  - ```$ fastboot flash boot boot.img```
  - ```$ fastboot flash system system.img```
  - ```$ fastboot falsh vendor vendor.img```
  - ```$ fastboot reboot```

**7) Post-Installation**

- Flash [vendor-fix-zip](https://forum.xda-developers.com/nexus-9/development/fix-build-prop-variety-fix-aka-contact-t3133347) for "Internal Error" message.
- Check [SuperSU Version](http://www.supersu.com/download), download, and flash
  - wipe dalvik and cache
- Flash [Gapps](http://opengapps.org/) (ARCH = ARM64)
  - wipe dalvik and cache
- Reboot

---

#### References:

- [Setup Build Environment](https://source.android.com/source/initializing)
- [Gathering Source](https://source.android.com/source/downloading)
- [Preparing to Build](https://source.android.com/source/building)
- [Arch Linux Wiki - Building Android](https://wiki.archlinux.org/index.php/android#Setting_up_the_build_environment)
- [Running Builds](https://source.android.com/source/running)
