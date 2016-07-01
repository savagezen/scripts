#!/usr/bin/sh

# Helper script for conky + dzen2 bug count popup
# chkrootkit - skips "possible" and "not tested"
# rkhunter - skips "skipped"

CHKi=$(cat /tmp/chkrootkit.daily | grep INFECTED | wc -l)
RKHw=$(cat /tmp/rkhunter.daily | grep Warning | wc -l)
TOTAL=$(($CHKi+$RKHw))

echo $TOTAL > /tmp/bugcount
