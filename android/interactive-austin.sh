# Author:  Austin Haedicke / gtbjj @ github
# Device:  Nexus 6P (Angler)
# Notes:   Please give credit when using this in your work!
#   Based on Cyan Lion profile by xSilas43
#   https://androidfilehost.com/?fid=24391638059060083

CODENAME=austin
VERSION=0.6
echo ----------------------------------------------
echo Applying $CODENAME v.$VERSION Profile Settings

CPU0=/sys/devices/system/cpu/cpu0/cpufreq/interactive
CPU4=/sys/devices/system/cpu/cpu4/cpufreq/interactive

echo ----------------------------------------------
echo Appling I/O scheduler and settings
echo > 5120 /sys/block/mmcblk0/queue/read_ahead_kb
echo noop > /sys/block/mmcblk0/queue/scheduler
echo fiops > /sys/block/mmcblk0/queue/scheduler

# change permissions and set governor
echo ----------------------------------------------
echo Changing governor and permissions
chmod 644 $CPU0/cpu_freq/scaling_governor
echo interactive > $CPU0/cpu_freq/scaling_governor
chmod 444 $CPU0/cpu_freq/scaling_governor
echo 1 > $CPU4/online
chmod 644 $CPU4/cpufreq/scaling_governor
echo interactive > $CPU4/cpu_freq/scaling_governor
chmod 444 $CPU4/cpu_freq/scaling_governor

# apply settings to LITTLE cluster
echo ----------------------------------------------
echo Applying settings to LITTLE cluster
echo 99 > $CPU0/go_hispeed_load
echo 50000 672000:60000 864000:20000 > $CPU0/above_hispeed_delay 
echo 50000 > $CPU0/timer_rate
echo 384000 > $CPU0/cpufreq/interactive/hispeed_freq 
echo 80000 > $CPU0/cpufreq/interactive/timer_slack
echo 75 460000:69 600000:80 672000:12 768000:14 864000:13 960000:69 1248000:84 1344000:8 1478400:10 1555200:86 > $CPU0/cpufreq/interactive/target_loads
echo 80000 > $CPU0/cpufreq/interactive/min_sample_time
echo 0 > $CPU0/cpufreq/interactive/align_windows
echo 1 > $CPU0/cpufreq/interactive/use_migration_notif
echo 0 > $CPU0/cpufreq/interactive/use_sched_load
echo 80000 > $CPU0/cpufreq/interactive/max_freq_hysteresis
echo 80000 > $CPU0/cpufreq/interactive/boostpulse_duration

# apply settings to Big cluster
echo ----------------------------------------------
echo Applying settings to Big cluster
echo 99 > $CPU4/cpufreq/interactive/go_hispeed_load
echo 40000 > $CPU4/cpufreq/interactive/above_hispeed_delay
echo 50000 > $CPU4/cpufreq/interactive/timer_rate
echo 1958400 > $CPU4/cpufreq/interactive/hispeed_freq
echo 80000 > $CPU4/cpufreq/interactive/timer_slack
echo 72 480000:25 633600:74 768000:21 864000:13 960000:11 1248000:30 1344000:8 1440000:7 1536000:7 1632000:6 1728000:6 1824000:6 1958400:7> $CPU4/cpufreq/interactive/target_loads 
echo 70000 > $CPU4/cpufreq/interactive/min_sample_time
echo 0 > $CPU4/cpufreq/interactive/align_windows
echo 1 > $CPU4/cpufreq/interactive/use_migration_notif
echo 0 > $CPU4/cpufreq/interactive/use_sched_load
echo 80000 > $CPU4/cpufreq/interactive/max_freq_hysteresis
echo 80000 > $CPU4/cpufreq/interactive/boostpulse_duration

# disabling touch and input boost
echo ----------------------------------------------
echo Disabling toucboost and input boost
echo 0:0 1:0 2:0 3:0 4:0 5:0 6:0 7:0 > /sys/module/cpu_boost/parameters/input_boost_freq 
echo 0 > /sys/module/cpu_boost/parameters/boost_ms
echo 0 > /sys/module/cpu_boost/parameters/input_boost_ms
echo 0 > /sys/module/msm_performance/parameters/touchboost

echo ----------------------------------------------\
echo Settings Successfully Applied!
