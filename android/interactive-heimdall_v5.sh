# Original settings by hEiMDaLL
# https://onedrive.live.com/?authkey=%21AEvS6yncruE8Ki0&id=C9E77668F08DB9DD%2155606&cid=C9E77668F08DB9DD
#
# Script by gtbjj @ GitHub

echo "Applying Interactive CPU governor"
echo 1 > /sys/devices/system/cpu/cpu4/online
chmod 644 /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
chmod 644 /sys/devices/system/cpu/cpu4/cpufreq/scaling_governor
echo interactive > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
echo interactive > /sys/devices/system/cpu/cpu4/cpufreq/scaling_governor
chmod 444 /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
chmod 444 /sys/devices/system/cpu/cpu4/cpufreq/scaling_governor

echo "Applying settings to LITTLE cluster"
echo 384000 > /sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq 
echo 1555200 > /sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq 
echo 96 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/go_hispeed_load 
echo 0 672000:20000 960000:40000 1344000:50000 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/above_hispeed_delay
echo 50000 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/timer_rate 
echo 672000 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/hispeed_freq 
echo -1 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/timer_slack 
echo 95 384000:88 460800:80 600000:79 672000:79 768000:79 864000:80 960000:86 1248000:91 1344000:97 1478400:99 1555200:99 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/target_loads 
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
echo 50000 960000:40000 1632000:50000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/above_hispeed_delay 
echo 60000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/timer_rate 
echo 633600 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/hispeed_freq 
echo -1 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/timer_slack 
echo 95 384000:76 480000:65 633600:76 768000:79 864000:80 960000:89 1248000:90 1344000:85 1440000:82 1536000:95 1632000:89 1728000:95 1824000:94 1958400:99 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/target_loads 
echo 60000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/min_sample_time 
echo 0 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/boost 
echo 0 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/align_windows 
echo 1 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/use_migration_notif 
echo 0 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/use_sched_load 
echo 80000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/max_freq_hysteresis 
echo 60000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/boostpulse_duration 

echo "Applying boost settings"
echo 0:600000 1:600000 2:600000 3:600000 4:633600 5:633600 6:633600 7:633600 > /sys/module/cpu_boost/parameters/input_boost_freq 
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
