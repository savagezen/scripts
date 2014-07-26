#!/bin/sh
# Mobile Music Sync

# Required programs
# - rsync
# - openssh
# - ssh client for android

echo "Has a profile been created for the target client? <y/n>  "
read client
if [[ "$client" == "y" ]] ; then
	# Profile has been previously created
	echo "Enter profile name:  "
	read prof_name
	src_dir=$(cat ~/.ssh/config | grep music_src-$prof_name | tail -c +22)
	tgt_dir=$(cat ~/.ssh/config | grep music_tgt-$prof_name | tail -c +22)
	rsync -avz $src_dir $prof_name:$tgt_dir
else
	# Profile has not been created
	echo "Do you want to create a profile for this client? <y/n>  "
	read profile
	if [[ "$profile" == "y" ]] ; then
		# No profile but DO create one
		echo "Enter a profile name:  "
		read prof_name
		echo "Enter phone user name:  "
		read rmt_usr
		echo "Enter phone ip address:  " 
		read rmt_addr
		echo "Host	$prof_name" >> ~/.ssh
		echo "		HostName $rmt_addr" >> ~/.ssh/config
		echo "		User $rmt_usr" >> ~/.ssh/config
		echo "Enter /path/to/target/directory:  " 
		read tgt_dir
		echo "#	music_tgt-$prof_name:  $tgt_dir" >> ~/.ssh/config
		echo "Enter /path/to/source/directory/:  "
		read src_dir
		echo "#	music_src-$prof_name:  $src_dir" >> ~/.ssh/config
		rsync -avz $src_dir $rmt_usr@$rmt_addr:$rmt_tgt
	else
		# No profile and DO NOT create one
		echo "Enter phone user name:  "
		read rmt_usr
		echo "Enter phone ip address:  " 
		read rmt_addr
		echo "Enter /path/to/target/directory:  " 
		read tgt_dir
		echo "Enter /path/to/source/directory/:  " 
		read src_dir
		rsync -avz $src_dir $rmt_usr@$rmt_addr:$tgt_dir
	fi
fi