#### Building AOSiP from Source

---

1) Initialize

```
$ mkdir aosip
$ cd aosip
$ repo init -u https://github.com/AOSiP/platform_manifest.git -b nougat-mr2
```

2) Sync

```
INITIAL
$ repo sync -c -f -j4 --force-sync --no-clone-bundle --no-tags

SUBSEQUENT
$ ./sync.sh
```

3) Build

```
$ virtualenv2 venv
$ . venv/bin/activate
$ . build/envsetup.sh
$ lunch aosip_angler-userdebug
$ make -j2 kronic
```

---

#### Reference:

- [Official Guide](https://github.com/AOSIP/platform_manifest)
