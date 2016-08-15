#Author: Austin Haedicke / gtbjj
#Device: Nexus 6P (Angler)
#Notes: Please give credit when using this in your work!
#Script Format and permissions:  Alcolawl's Ghost Pepper Script

CODENAME=austin
VERSION=0.3

echo ---------------------------------------------------------------------
echo Applying $CODENAME  v.$VERSION Interactive Governor Settings
echo ---------------------------------------------------------------------

#echo Applying IO Scheduler and settings
#echo ----------------------------------
#echo NOOP settings will be applied first,
#echo "then FIOPS if it is avaialable."

#echo noop > /sys/block/mmcblk0/queue/scheduler
#echo fiops > /sys/block/mmcblk0/queue/scheduler

#Apply settings to LITTLE cluster
echo -----------------------------------
echo Applying settings to LITTLE cluster

#Temporarily change permissions to governor files for the LITTLE cluster to enable Interactive governor
chmod 644 /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
echo interactive > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
chmod 444 /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor

#Tweak Interactive Governor
echo 75 460000:69 600000:30 672000:12 768000:80 864000:13 960000:11 1248000:30 1344000:82 1478000:10 1555000:0 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/target_loads
echo 10000 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/above_hispeed_delay
echo 460000 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/hispeed_freq 
echo 10000 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/timer_rate
#echo 10000 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/min_sample_time
#echo 0 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/boostpulse_duration
#echo 8000 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/timer_slack
#echo 0 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/boost
#echo 0 > /sys/devices/system/cpu/cpu0/cpufreq/interactive/max_freq_hysteresis # lower for performance, raise for battery

#Apply settings to Big cluster
echo --------------------------------
echo Applying settings to Big cluster

#Temporarily change permissions to governor files for the Big cluster to enable Interactive governor
echo 1 > /sys/devices/system/cpu/cpu4/online								#Online Core 4
chmod 644 /sys/devices/system/cpu/cpu4/cpufreq/scaling_governor
echo interactive > /sys/devices/system/cpu/cpu4/cpufreq/scaling_governor
chmod 444 /sys/devices/system/cpu/cpu4/cpufreq/scaling_governor

#Temporarily change permissions to governor files for the Big cluster to change minimum frequency to 633MHz
chmod 644 /sys/devices/system/cpu/cpu4/cpufreq/scaling_min_freq
echo 633600 > /sys/devices/system/cpu/cpu4/cpufreq/scaling_min_freq		#Core 4 Minimum Frequency = 633MHz
chmod 444 /sys/devices/system/cpu/cpu4/cpufreq/scaling_min_freq

#Tweak Interactive Governor
echo 72 480000:25 633000:32 768000:21 864000:13 960000:11 1248000:30 1344000:84 1440000:7 1536000:7 1632000:6 1728000:6 1824000:6 1958000:0 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/target_loads
echo 1440000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/hispeed_freq
echo 10000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/above_hispeed_delay
echo 10000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/timer_rate 
#echo 20000 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/min_sample_time # 40000 Ghost Pepper
#echo 0 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/max_freq_hysteresis
#echo 0 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/boostpulse_duration
#echo -1 > /sys/devices/system/cpu/cpu4/cpufreq/interactive/timer_slack

#Disable TouchBoost
echo --------------------
echo Disabling TouchBoost
echo 0 > /sys/module/msm_performance/parameters/touchboost

#Disable Core Control and Enable Thermal Throttling allowing for longer sustained performance
echo Disabling Aggressive CPU Thermal Throttling
echo 0 > /sys/module/msm_thermal/core_control/enabled
echo Y > /sys/module/msm_thermal/parameters/enabled
echo ------------------------------
echo Settings Successfully Applied!
echo ------------------------------
