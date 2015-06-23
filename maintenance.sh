#!/bin/zsh

#Filesystem defragment, scrub, blance
find / -xdev -type d -print -exec btrfs filesystem defragment '{}' \;
btrfs scrub start /								# verify checksums on metadata
btrfs balance start /								# reorganize big data chunks

# Mirrorlist
pacman -Syy											# for refresh of all mirrors
cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.backup					# backup mirrorlist
reflector --country 'United States' -l 50 -p http --sort rate --save /etc/pcman.d/mirrorlist	# 50 most recent sorted by speed
pacman -Syy											# sync to new mirrorlist
 
# Packages / Pacman
pacman-optimize
pacman -Rns $(pacman -Qtdq)	# recursively uninstall orphans
paccache -r			# keep 3 most recent version of installed packages
paccache -ruk0			# remove cached versions of unistalled packages
