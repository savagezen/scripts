# Settings by xSilas43
# https://www.androidfilehost.com/?fid=24391638059060083
#
# Script by gtbjj @ GitHub

echo "Setting Interactive governor"
echo 1 > /sys/devices/system/cpu/cpu4/online
chmod 644 /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
chmod 644 /sys/devices/system/cpu/cpu4/cpufreq/scaling_governor
echo interactive > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
echo interactive > /sys/devices/system/cpu/cpu4/cpufreq/scaling_governor
chmod 444 /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
chmod 444 /sys/devices/system/cpu/cpu4/cpufreq/scaling_governor

echo "Applying settings to LITTLE cluster"
echo 91 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/go_hispeed_load 
echo 0 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/above_hispeed_delay 
echo 60000 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/timer_rate 
echo 960000 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/hispeed_freq 
echo 480000 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/timer_slack 
echo 80 460800:70 600000:99 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/target_loads 
echo 0 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/min_sample_time 
echo 0 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/boost 
echo 1 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/align_windows 
echo 1 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/use_migration_notif 
echo 0 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/use_sched_load 
echo 0 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/max_freq_hysteresis 
echo 0 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/boostpulse_duration 

echo "Applying settings to Big cluster"
echo 633600 > /sys/devices/system/cpu/cpu4/cpufreq/scaling_min_freq 
echo 91 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/go_hispeed_load 
echo 0 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/above_hispeed_delay 
echo 30000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/timer_rate 
echo 960000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/hispeed_freq 
echo 480000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/timer_slack 
echo 70 960000:90 1440000:99 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/target_loads 
echo 0 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/min_sample_time 
echo 0 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/boost 
echo 1 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/align_windows 
echo 1 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/use_migration_notif 
echo 0 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/use_sched_load 
echo 0 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/max_freq_hysteresis 
echo 0 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/boostpulse_duration 

echo "Applying boost settings"
echo 1 > /sys/module/cpu_boost/parameters/input_boost_enabled 
echo 0:600000 1:600000 2:600000 3:600000 4:0 5:0 > /sys/module/cpu_boost/parameters/input_boost_freq 
echo 0 > /sys/module/cpu_boost/parameters/boost_ms 
echo 1920 > /sys/module/cpu_boost/parameters/input_boost_ms 
echo 0 > /sys/module/msm_performance/parameters/touchboost 
