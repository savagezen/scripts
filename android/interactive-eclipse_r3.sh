# Settings published by xSilas43
# https://androidfilehost.com/?fid=24438995911972631
#
# Script by gtbjj @ GitHub

echo "Setting Interactive CPU govenror"
echo 1 > /sys/devices/system/cpu/cpu4/online
chmod 644 /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
chmod 644 /sys/devices/system/cpu/cpu4/cpufreq/scaling_governor
echo interactive > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
echo interactive > /sys/devices/system/cpu/cpu4/cpufreq/scaling_governor
chmod 444 /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
chmod 444 /sys/devices/system/cpu/cpu4/cpufreq/scaling_governor

echo "Applying settings to LITTLE cluster"
echo 40000 864000:50000 1248000:40000 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/above_hispeed_delay
echo 50000 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/timer_rate 
echo 960000 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/hispeed_freq 
echo -1 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/timer_slack 
echo 95 384000:75 460000:76 600000:80 672000:80 768000:80 864000:82 960000:85 1248000:86 1344000:87 1478000:87 1555000:87 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/target_loads 
echo 90000 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/min_sample_time 
echo 0 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/align_windows 
echo 1 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/use_migration_notif 
echo 1 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/use_sched_load 
echo 0 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/max_freq_hysteresis 
echo 0 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/boostpulse_duration 

echo "Applying settings to Big cluster"
echo 80 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/go_hispeed_load 
echo 50000 1440000:20000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/above_hispeed_delay 
echo 50000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/timer_rate 
echo 633000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/hispeed_freq 
echo -1 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/timer_slack 
echo 95 633000:75 768000:80 864000:81 960000:81 1248000:85 1344000:85 1440000:85 1536000:85 1632000:86 1728000:86 1824000:87 1958400:87 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/target_loads 
echo 80000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/min_sample_time 
echo 0 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/align_windows 
echo 1 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/use_migration_notif 
echo 1 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/use_sched_load 
echo 0 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/max_freq_hysteresis 
echo 0 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/boostpulse_duration 

echo "Applying boost settings"
echo 1 > /sys/module/cpu_boost/parameters/input_boost_enabled 
echo 0:960000 1:960000 2:960000 3:960000 4:0 5:0 6:0 7:0 > /sys/module/cpu_boost/parameters/input_boost_freq 
echo 0 > /sys/module/cpu_boost/parameters/boost_ms 
echo 40 > /sys/module/cpu_boost/parameters/input_boost_ms 
echo 0 > /sys/module/msm_performance/parameters/touchboost 
