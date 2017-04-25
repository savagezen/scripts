#### Building AOSP From Source (Nexus 6P - Angler)
---

**1) Gathering Source**

See latest [code name releases ](https://source.android.com/source/build-numbers#source-code-tags-and-builds) that correspond to repo branch.

```
$ mkdir android
$ cd android

$ git config --global user.name "Your Name"
$ git config --global user.email "you@example.com"

$ repo init -u https://android.googlesource.com/platform/manifest -b CODENAME_RELEASE
$ time repo sync -j3
```

**2) Proprietary Binaries**

Download [vendor image](https://developers.google.com/android/drivers#angler) that matches the ```Build``` of the above repo branch, then:

```
$ tar -xvf huawei-angler-VENORNUMVER-BUILDNUMBER.tgz
$ sh extract-huawe-angler.sh

NOTE - Press 'Enter' to view license, once viewing press CTL + C to skip to agreement.
```

**3) Preparation**

```
$ virtualenv2 venv
$ source venv/bin/activate

NOTE:  Make sure Android looks for Java in the right place
$ export JAVA_HOME=/usr/lib/jvm/java-x-openjdk

$ make clobber
$ source build/envsetup.sh
$ lunch aosp_angler-userdebug
```

**4) Customization**

**5) Build**

```
$ time make -j2

```

**6) Installation**

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

- Install Gapps

---

#### References:

- [Setup Build Environment](https://source.android.com/source/initializing)
- [Gathering Source](https://source.android.com/source/downloading)
- [Preparing to Build](https://source.android.com/source/building)
- [Arch Linux Wiki - Building Android](https://wiki.archlinux.org/index.php/android#Setting_up_the_build_environment)
- [Running Builds](https://source.android.com/source/running)
- [Add OpenGapps](https://github.com/opengapps/aosp_build)
