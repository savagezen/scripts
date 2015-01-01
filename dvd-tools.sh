#!/bin/sh
# CD / DVD - Rip, Burn, Play

# Functions
menu () {
  echo -e "What would you like to do:\n
  [1] Play DVD / ISO
  [2] Create ISO from DVD
  [3] Create ISO from Directory
  [4] Burn ISO to DVD
  [5] Format and Erase CD / DVD + RW
  [6] Exit\n"
  echo -n "Selection: " && read MENU_OPT

  if [ "$MENU_OPT" == "1" ] ; then
	play
  elif [ "#MENU_OPT" == "2" ] ; then
	iso_from_dvd
  elif [ "$MENU_OPT" == "3" ] ; then
	iso_from_directory
  elif [ "$MENU_OPT" == "4" ] ; then
	burn
  elif [ "$MENU_OPT" == "5" ] ; then
	format
  else
	exit
  fi
}

play () {
  echo -n "Which would you like to play? (dvd / iso): " && read PLAY_CHOICE
  if [ "$PLAY_CHOICE" == "dvd" ] ; then
	mpv dvd:// --dvd-device=/dev/sr0	
  elif [ "$PLAY_CHOICE" == "iso" ] ; then
	echo -n "Enter /path/to/image.iso: " && read ISO_LOC
	mpv $ISO_LOC
  fi
}

iso_from_dvd () {
  echo -n "Enter Title: " && read ISO_TITLE
  dd if=/dev/sr0 of=$ISO_TITLE.iso
  menu
}

iso_from_directory () {
  echo -n "Enter Full Path of Directory Containing Files: " && read FOR_ISO
  echo -n "Enter Title of Movie for ISO: " && read ISO_TITLE
  genisoimage -V "$ISO_TITLE" -J -r -o $ISO_TITLE.iso $FOR_ISO
  menu
}

burn () {
  echo -n "Enter path/to/image.iso (EX: $(ls *.iso)): " && read ISO_IMG
  growisofs -dvd-compat -Z /dev/sr0=$ISO_IMG
  menu
}

format () {
  ## Alternate:			$ cdrecord -V dev=/dev/sr0 blank=all
  ## Format Without Erasing:	$ dvd+rw-format -force /dev/sr0
  dvd+rw-format -blank=full /dev/sr0
  menu
}

# Main
menu
