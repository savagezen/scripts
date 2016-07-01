#!/usr/bin/sh
# bluetooth scripts for Asus X205TA

sudo systemctl start bluetooth
sudo systemctl start btattach

sudo hciconfig hci0 up

bluetoothctl
