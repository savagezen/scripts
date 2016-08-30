# Author:  Austin Haedicke / gtbjj @ github
# Device:  Nexus 6P (Angler)
# Notes:   Please give credit when using this in your work!
#          - Script format and permissions by Alcolawl
#          - Selectged profile (settings) by soniCron and Heimdal

# Interactive Governor Settings:
#   target_loads		frequency:preference, 90 is default
#   min_sample_time		time to spend before ramping down
#   above_hispeed_delay		when at hispeed_freq ait this long before ramping up
#   hipseed_freq		temp freq while deciding to ramp up/down after go_hispeed_load
#   go_hispeed_load		% load at which to ramp to hispeed_freq
#   timer_rate			re-evaluate CPU after this long when ramping up
#   timer_slack			governor will always run after this long
#   max_freq_hysteresis		performance -> lower; battery -> higher
#   boost_pulse_duration	hold CPU at hispeed_freq on write to boost_pulse
#   boost			if not 0, boost all CPUs to hispeed_freq until 0 is written
#   input_boost			if not 0, boost all CPUs to hispeed_freq on CPU input

# Scheduler Prefernce::
#   battery		NOOP
#   performance		FIOPS
#   multitasking	BFQ
#   gaming		Deadline

# Scheduler Settings:
#   read_ahead_kb	size of recently used files to keep ready, 1024 default
#   async_scale
#   read_scale
#   sync_scale
#   write_scale


CODENAME=austin
VERSION=0.4
CPU0=/sys/devices/system/cpu/cpu0
CPU4=/sys/devices/system/cpu/cpu4
echo ----------------------------------------------
echo Applying $CODENAME v.$VERSION Profile Settings


echo ----------------------------------------------
echo Appling I/O scheduler and settings
# echo > /sys/block/mmcblk0/queue/read_ahead_kb
echo noop > /sys/block/mmcblk0/queue/scheduler
echo fiops > /sys/block/mmcblk0/queue/scheduler


echo ----------------------------------------------
echo Temporarily change permissions to governor
echo files for LITTLE cluster to enable interactive
echo governor
chmod 644 $CPU0/scaling_governor
echo interactive > $CPU0/scaling_governor
chmod 444 $CPU0/scaling_governor


echo ----------------------------------------------
echo Applying settings to LITTLE CPU cluster
echo 75 460000:69 600000:80 672000:12 768000:14 864000:13 960000:69 1248000:84 1344000:8 1478400:10 1555200:99 > $CPU0/cpufreq/interactive/target_loads
echo 0 384000:20000 460000:10000 600000:10000 960000:20000 1248000:10000 > $CPU0/cpufreq//interactive/above_hispeed_delay
echo 384000 > $CPU0/cpufreq/interactive/hispeed_freq	# most used freq
echo 80000 > $CPU0/cpufreq/interactive/timer_rate # drop until laggy
echo 80000 > $CPU0/cpufreq/interactive/min_sample_time # drop until laggy
echo 60000 > $CPU0/cpufreq/interactive/max_freq_hysteresis # 80000 if poor battery, 0 if poor performance
echo 200 > $CPU0/cpufreq/interactive/go_hispeed_load
echo -1 > $CPU0/cpufreq/interactive/timer_slack
echo 0 > $CPU0/cpufreq/interactive/boost_pulse_duration


echo ----------------------------------------------
echo Temporarily change permissions to governor
echo files for Big cluster to enable interactive
echo governor and to set minimum frequency
echo 1 > $CPU4/online
chmod 644 $CPU4/cpufreq/scaling_governor
echo interactive > $CPU4/cpufreq/scaling_governor
chmod 444 $CPU4/cpufreq/scaling_governor
chmod 644 $CPU4/cpufreq/scaling_min_freq
chmod 644 $CPU4/cpufreq/scaling_min_freq
echo 384000 > $CPU4/cpufreq/scaling_min_freq
chmod 444 $CPU4/cpufreq/scaling_min_freq


echo ----------------------------------------------
echo Applying settings to Big CPU cluster
echo 72 480000:25 633600:74 768000:21 864000:13 960000:11 1248000:30 1344000:8 1440000:7 1536000:7 1632000:6 1728000:6 1824000:6 1958400:7 > $CPU4/cpufreq/interactive/target_loads
echo 0 384000:50000 633000:50000 864000:10000 960000:10000 1248000:20000 > $CPU4/cpufreq/interactive/above_hispeed_delay
echo 384000 > $CPU4/cpufreq/interactive/hispeed_freq	# most used freq
echo 10000 > $CPU4/cpufreq/interactive/timer_rate # raise if laggy
echo 10000 > $CPU4/cpufreq/interactive/min_sample_time # raise if laggy
echo 20 > $CPU4/cpufreq/interactive/go_hispeed_load # 99 if battery poor
echo 0 > $CPU4/cpufreq/interactive/max_freq_hysteresis
echo -1 > $CPU4/cpufreq/interactive/timer_slack
echo 0 > $CPU4/cpufreq/interactive/boostpulse_duration

echo ----------------------------------------------
echo Disabling TouchBoost
echo 0 > /sys/module/msm_performance/parameters/touchboost
#Disable Core Control and Enable Thermal Throttling allowing for longer sustained performance
echo Disabling Aggressive CPU Thermal Throttling
echo 0 > /sys/module/msm_thermal/core_control/enabled 
echo Y > /sys/module/msm_thermal/parameters/enabled

echo ----------------------------------------------
echo Disabling Input Boost
echo 0:0 1:0 2:0 3:0 4:0 5:0 6:0 7:0 > /sys/module/cpu_boost/parameters/input_boost_freq

echo ----------------------------------------------
echo Settings Successfully Applied!
echo ----------------------------------------------

