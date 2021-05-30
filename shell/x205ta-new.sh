#!/bin/sh
#create bootable ArchUSB for ASUS X205TA

USB=/dev/sdc
USB_DIR=/mnt
ISO_VERSION=$(date +%Y.%m).01
ISO_MIRROR=https://mirrors.edge.kernel.org/archlinux/iso/$ISO_VERSION/archlinux-$ISO_VERSION-x86_64.iso
BOOTIA_SRC=https://github.com/jfwells/linux-asus-t100ta/raw/master/boot/bootia32.efi
GRUB_SRC=https://raw.githubusercontent.com/savagezen/x205ta/master/grub.cfg

# fetching sources
curl -o /tmp/archlinux.iso $ISO_MIRROR
curl -o /tmp/bootia32.efi $BOOTIA_SRC
curl -o /tmp/grub.cfg $GRUB_SRC

# format disk
sudo parted $USB mkpart ARCH_$(date +%Y%m) FAT32 1MiB 100%
sudo mkfs.vfat -F 32 -n ARCH_$(date +%Y%m) $USB
sudo mount $USB $USB_DIR

# write image
sudo bsdtar -x --exclude=isolinux/ --exclude=EFI/archiso/ --exclude=/arch/boot/syslinux/ -f /tmp/archlinux.iso -C $USB_DIR
sudo cp /tmp/bootia32.efi $USB_DIR/EFI/boot/
sed -i "s/ARCH_.*/$ARCH_$(date +%Y%m)/" /tmp/grub.cfg
sudo cp /tmp/grub.cfg $USB_DIR

# clean up
rm /tmp/archlinux.iso
rm /tmp/bootia32.efi
rm /tmp/grub.cfg

echo "On GRUB prompt:"
echo "$ configfile /grub.cfg"
echo " "
echo "On Arch prmpt:"
echo "enable wifi > see https://wiki.archlinux.org/title/ASUS_x205ta#Enable_wifi"
