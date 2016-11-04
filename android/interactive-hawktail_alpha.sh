# Settings published by soniCron
# https://www.androidfilehost.com/?fid=24588232905722751
#
# Script by gtbjj @ GitHub

echo "Switching to Interactive governor"
# temporarily change permissions to set governor
chmod 644 /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
echo 1 > /sysdevices/cpu/cpu4/online
chmod 644 /sys/devices/system/cpu/cpu4/cpufreq/scaling_governor
echo interactive > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
echo interactive > /sys/devices/system/cpu/cpu4/cpufreq/scaling_governor
chmod 444 /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
chmod 444 /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor

echo "Applying settings to LITTLE cluster"
echo 95 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/go_hispeed_load 
echo 0 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/above_hispeed_delay 
echo 60000 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/timer_rate 
echo 1248000 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/hispeed_freq 
echo -1 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/timer_slack 
echo 70 460800:58 600000:82 672000:72 768000:94 864000:83 960000:99 1248000:75 1478400:68 1555200:99 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/target_loads 
echo 120000 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/min_sample_time 
echo 0 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/boost 
echo 0 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/align_windows 
echo 1 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/use_migration_notif 
echo 0 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/use_sched_load 
echo 120000 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/max_freq_hysteresis 
echo 80000 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/boostpulse_duration 

echo "Applying settings to Big cluster"
echo 633600 > /sys/devices/system/cpu/cpu4/cpufreq/scaling_min_freq 
echo 90 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/go_hispeed_load 
echo 0 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/above_hispeed_delay 
echo 60000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/timer_rate 
echo 1824000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/hispeed_freq 
echo -1 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/timer_slack 
echo 74 768000:73 864000:64 960000:80 1248000:61 1344000:69 1440000:64 1536000:74 1632000:69 1728000:69 1824000:72 1948000:99 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/target_loads 
echo 120000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/min_sample_time 
echo 0 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/boost 
echo 0 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/align_windows 
echo 1 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/use_migration_notif 
echo 0 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/use_sched_load 
echo 60000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/max_freq_hysteresis 
echo 80000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/boostpulse_duration 

echo "Enabling input boost and disabling touchboost"
echo 1 > /sys/module/cpu_boost/parameters/input_boost_enabled 
echo 0:960000 1:960000 2:960000 3:960000 4:0 5:0 > /sys/module/cpu_boost/parameters/input_boost_freq 
echo 0 > /sys/module/cpu_boost/parameters/boost_ms 
echo 50 > /sys/module/cpu_boost/parameters/input_boost_ms 
echo 0 > /sys/module/msm_performance/parameters/touchboost 

