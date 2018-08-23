# Original Heimdall settings by Heimdall
# https://onedrive.live.com/?authkey=%21AEvS6yncruE8Ki0&id=C9E77668F08DB9DD%2155606&cid=C9E77668F08DB9DD
#
# Heimdall Remix RC3
# Script and settings by gtbjj @ GitHub

echo "Setting Interactive cpu governor"
echo 1 > /sys/devices/system/cpu/cpu4/online
chmod 644 /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
chmod 644 /sys/devices/system/cpu/cpu4/cpufreq/scaling_governor
echo interactive > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
echo interactive > /sys/devices/system/cpu/cpu4/cpufreq/scaling_governor
chmod 444 /sys/devices/system/cpu/cpu0/cpufreq/scaling_govnernor
chmod 444 /sys/devices/system/cpu/cpu4/cpufreq/scaling_governor

echo "Applying settings to LITTLE cluster"
echo 384000 > /sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq 
echo 1555200 > /sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq 
echo 96 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/go_hispeed_load 
echo 0 384000:20000 460000:10000 600000:10000 960000:20000 1248000:10000 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/above_hispeed_delay 
echo 50000 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/timer_rate 
echo 384000 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/hispeed_freq 
echo -1 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/timer_slack 
echo 75 460000:69 600000:80 672000:12 768000:14 864000:13 960000:69 1248000:84 1344000:8 1478400:10 1555200:86 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/target_loads 
echo 80000 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/min_sample_time 
echo 0 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/boost 
echo 0 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/align_windows 
echo 1 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/use_migration_notif 
echo 0 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/use_sched_load 
echo 80000 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/max_freq_hysteresis 
echo 60000 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/boostpulse_duration 

echo "Applying settings to Big cluster"
echo 384000 > /sys/devices/system/cpu/cpu4/cpufreq/scaling_min_freq 
echo 1958400 > /sys/devices/system/cpu/cpu4/cpufreq/scaling_max_freq 
echo 20 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/go_hispeed_load 
echo 0 384000:50000 633000:50000 864000:10000 960000:10000 1248000:20000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/above_hispeed_delay 
echo 60000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/timer_rate
echo 384000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/hispeed_freq 
echo -1 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/timer_slack 
echo 72 480000:25 633600:74 768000:21 864000:13 960000:11 1248000:30 1344000:8 1440000:7 1536000:7 1632000:6 1728000:6 1824000:6 1958400:7 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/target_loads 
echo 60000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/min_sample_time 
echo 0 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/boost 
echo 0 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/align_windows 
echo 1 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/use_migration_notif 
echo 0 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/use_sched_load 
echo 80000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/max_freq_hysteresis 
echo 60000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/boostpulse_duration 

echo "Applying boost settings"
echo 0:600000 1:600000 2:60000 0 3:600000 4:633600 5:633600 6:633600 7:633600 > /sys/module/cpu_boost/parameters/input_boost_freq 
echo 1248000 > /sys/module/cpu_boost/parameters/sync_threshold 
echo 40 > /sys/module/cpu_boost/parameters/boost_ms 
echo 15 > /sys/module/cpu_boost/parameters/migration_load_threshold 
echo Y > /sys/module/cpu_boost/parameters/load_based_syncs 
echo N > /sys/module/cpu_boost/parameters/shed_boost_on_input 
echo 300 > /sys/module/cpu_boost/parameters/input_boost_ms 
echo 1 > /sys/module/cpu_boost/parameters/input_boost_enabled 
echo 0 > /sys/module/msm_performance/parameters/touchboost 
echo 0 > /sys/module/msm_thermal/core_control/enabled 
echo Y > /sys/module/msm_thermal/parameters/enabled 
