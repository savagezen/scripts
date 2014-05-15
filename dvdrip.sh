#!/bin/sh
# Rip DVD / CD

echo -n "Enter source device (/dev/sr0):  " && read source_dev
echo -n "Enter destination:  " && read destination
echo -n "Enter title:  " && read title
dd if=$source_dev of=$destination/$title.iso