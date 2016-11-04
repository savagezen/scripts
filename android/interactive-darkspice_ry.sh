# Settings published by xSilas43
# https://androidfilehost.com/?fid=24421527759885741
#
# Script by gtbjj @ GitHub

echo "Applying Interactive CPU governor"
echo 1 > /sys/devices/system/cpu/cpu4/online
chmod 644 /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
chmod 644 /sys/devices/system/cpu/cpu4/cpufreq/scaling_governor
echo interactive > /sys/devices/system/cpu/cpu0/scaling_governor
echo interactive > /sys/devices/system/cpu/cpu4/scaling_governor
chmod 444 /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
chmod 444 /sys/devices/system/cpu/cpu4/cpufreq/scaling_governor

echo "Applying settings to LITTLE cluster"
echo 200 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/go_hispeed_load 
echo 60000 768000:50000 960000:30000 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/above_hispeed_delay 
echo 50000 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/timer_rate 
echo 384000 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/hispeed_freq 
echo -1 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/timer_slack 
echo 95 384000:75 460000:30 600000:12 672000:14 768000:80 864000:11 960000:98 1248000:8 1344000:99 1478000:100 1555000:100 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/target_loads 
echo 85000 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/min_sample_time 
echo 0 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/align_windows 
echo 1 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/use_migration_notif 
echo 0 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/use_sched_load 
echo 0 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/max_freq_hysteresis 
echo 0 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/boostpulse_duration 

echo "Applying settings to Big cluster"
echo 200 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/go_hispeed_load 
echo 50000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/above_hispeed_delay 
echo 50000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/timer_rate 
echo 633000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/hispeed_freq 
echo -1 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/timer_slack 
echo 98 633000:74 768000:43 864000:11 960000:79 1248000:8 1344000:7 1440000:6 1536000:6 1632000:100 1728000:5 1824000:7 1958400:100 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/target_loads 
echo 75000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/min_sample_time 
echo 0 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/align_windows 
echo 1 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/use_migration_notif 
echo 0 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/use_sched_load 
echo 0 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/max_freq_hysteresis 
echo 0 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/boostpulse_duration 

echo "Applying boost settings"
echo 1 > /sys/module/cpu_boost/parameters/input_boost_enabled 
echo 0:672000 1:672000 2:672000 3:672000 4:0 5:0 6:0 7:0 > /sys/module/cpu_boost/parameters/input_boost_freq 
echo 0 > /sys/module/cpu_boost/parameters/boost_ms 
echo 40 > /sys/module/cpu_boost/parameters/input_boost_ms 
echo 0 > /sys/module/msm_performance/parameters/touchboost 
