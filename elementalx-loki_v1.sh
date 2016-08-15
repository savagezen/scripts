#Author: .hEiMDaLL. (Tobias Heinl)
#Credits to: xSilas43, SoniCron, Alcolawl, flar2
#Device: Nexus 6P (Angler) - possibly any SD810 device
#Codename: LOKI
#Build Status: Beta
#Version: 1
#Last Updated: 2016.02.27

#Notes: Please give credit when using this in your work!


echo ------------------------------------------------------
echo Applying 'LOKI' v1 Governor Settings by .heimdall.
echo ------------------------------------------------------
echo "These settings are for elementalx/interactive governor."
echo Make sure your kernel an ROM are supported and you
echo are using the correct version of this script for 
echo your device!
echo ------------------------------------------------------
echo Use of this script is, at all times, 'at your own risk.' 
echo I am not responsible to any user or third party for any 
echo damages whatsoever resulting from the use or inability 
echo to use this script
echo ------------------------------------------------------
echo Please give credit when using this in your work!
echo ------------------------------------------------------

echo Set IO Scheduler and Read ahead value: fiops, 1024kb
echo fiops > /sys/block/mmcblk0/queue/scheduler
echo 1024 > /sys/block/mmcblk0/queue/read_ahead_kb


#turn on all cores
echo Activating all available Cores
chmod 644 /sys/devices/system/cpu/online
echo 0-7 > /sys/devices/system/cpu/online
for i in 0 1 2 3 4 5 6 7
do 
chmod 644 /sys/devices/system/cpu/cpu$i/online
echo 1 > /sys/devices/system/cpu/cpu$i/online
done


#Apply settings to LITTLE cluster
echo Applying settings to LITTLE Cluster 384MHz to 1555MHz elementalx
#Temporarily change permissions to governor files for the LITTLE cluster to enable Interactive governor
chmod 644 /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
echo elementalx > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
chmod 444 /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
chmod 644 /sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq
echo 384000 > /sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq
chmod 444 /sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq
chmod 644 /sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq
echo 1555200 > /sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq
chmod 444 /sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq

#Tweak ElementalX Governor
echo 672000 > /sys/devices/system/cpu/cpu0/cpufreq/elementalx/active_floor_freq
echo 10 > /sys/devices/system/cpu/cpu0/cpufreq/elementalx/down_differential
echo 3 > /sys/devices/system/cpu/cpu0/cpufreq/elementalx/powersave
echo 1 > /sys/devices/system/cpu/cpu0/cpufreq/elementalx/sampling_down_factor
echo 100000 > /sys/devices/system/cpu/cpu0/cpufreq/elementalx/sampling_rate
#[[ -w /sys/devices/system/cpu/cpu0/cpufreq/elementalx/sampling_rate_min ]] && echo 10000 > /sys/devices/system/cpu/cpu0/cpufreq/elementalx/sampling_rate_min
echo 97 > /sys/devices/system/cpu/cpu0/cpufreq/elementalx/up_threshold

#Apply settings to Big cluster
echo Applying settings to LITTLE Cluster 384MHz to 1958MHz interactive
#Temporarily change permissions to governor files for the Big cluster to enable Interactive governor
chmod 644 /sys/devices/system/cpu/cpu4/cpufreq/scaling_governor
echo interactive > /sys/devices/system/cpu/cpu4/cpufreq/scaling_governor
chmod 444 /sys/devices/system/cpu/cpu4/cpufreq/scaling_governor
chmod 644 /sys/devices/system/cpu/cpu4/cpufreq/scaling_min_freq
echo 384000 > /sys/devices/system/cpu/cpu4/cpufreq/scaling_min_freq
chmod 444 /sys/devices/system/cpu/cpu4/cpufreq/scaling_min_freq
chmod 644 /sys/devices/system/cpu/cpu4/cpufreq/scaling_max_freq
echo 1958400 > /sys/devices/system/cpu/cpu4/cpufreq/scaling_max_freq
chmod 444 /sys/devices/system/cpu/cpu4/cpufreq/scaling_max_freq


#Tweak Interactive Governor
echo 20 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/go_hispeed_load
echo 20000 960000:40000 1632000:50000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/above_hispeed_delay
echo 50000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/timer_rate
echo 633000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/hispeed_freq
echo -1 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/timer_slack
echo 95 384000:45 480000:37 633600:74 768000:73 864000:74 960000:90 1248000:81 1344000:50 1440000:79 1536000:95 1632000:89 1728000:95 1824000:94 1958400:99 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/target_loads 
echo 60000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/min_sample_time
[[ -e /sys/devices/system/cpu/cpu4/cpufreq/interactive/boost ]] && echo 0 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/boost
echo 0 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/align_windows
echo 1 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/use_migration_notif
echo 0 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/use_sched_load
echo 80000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/max_freq_hysteresis
echo 0 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/boostpulse_duration


#Enable Input Boost for 600/633MHz for 666ms
echo Enabling Dual-Cluster Input Boost at 600,633MHz 
echo 0:600000 1:600000 2:600000 3:600000 4:633600 5:633600 6:633600 7:633600 > /sys/module/cpu_boost/parameters/input_boost_freq
echo 0 > /sys/module/cpu_boost/parameters/boost_ms
echo 666 > /sys/module/cpu_boost/parameters/input_boost_ms
[[ -e /sys/module/cpu_boost/parameters/input_boost_enabled ]] && echo 1 > /sys/module/cpu_boost/parameters/input_boost_enabled
#Disable TouchBoost
echo Disabling TouchBoost
[[ -e /sys/module/msm_performance/parameters/touchboost ]] && echo 0 > /sys/module/msm_performance/parameters/touchboost
#Disable Core Control and Enable Thermal Throttling allowing for longer sustained performance
echo Disabling Aggressive CPU Thermal Throttling
echo 0 > /sys/module/msm_thermal/core_control/enabled
echo Y > /sys/module/msm_thermal/parameters/enabled
echo ----------------------------------------------------
echo Settings Successfully Applied! 
echo You may now tweak them further in your prefered Kernel Tweaking App
echo ----------------------------------------------------




