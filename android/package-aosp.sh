#!/usr/bin/sh
# repackage ota with source built AOSP and kerenel - Nexus 6P

cd /tmp

# pull source
echo -n "Enter link for OTA update: "
read OTA_LINK
curl -o official_ota.zip OTA_LINK
tar -xvf official_ota.zip

