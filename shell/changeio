#!/bin/sh
# List and Change I/O Scheduler

echo -n "Current:  " && cat /sys/block/sda/queue/scheduler

echo -n "Change to:  " && read newsched
sudo echo -n "$newsched" > /sys/block/sda/queue/scheduler

echo -n "New:  " && cat /sys/block/sda/queue/scheduler 
