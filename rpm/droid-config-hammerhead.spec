# device is the android codename for the device (the bsp device)
# eg mako = Nexus 4
%define device hammerhead
# vendor is used in device/%vendor/%device/ (the vendor providing the bsp)
%define vendor lge

# Manufacturer and device name to be shown in UI
%define vendor_pretty LG
%define device_pretty Nexus 5

%define dcd_path ./

# Device-specific bluetoothd configuration
Provides: bluez-configs

# Device-specific bluetooth-rfkill-event configuration
Provides: bluetooth-rfkill-event-configs

# Device-specific obexd configuration
Requires: obexd-server >= 0.48+git8
Requires: obexd-calldata-provider >= 0.0.13
Provides: obexd-configs

# Make updates to work for old hacked images,
# this should be removed before releasing
Obsoletes: droid-hal-hammerhead-sailfish-config
Obsoletes: droid-hal-hammerhead-pulseaudio-settings
Obsoletes: droid-hal-hammerhead-preinit-plugin
Obsoletes: droid-hal-hammerhead-policy-settings


%include droid-configs-device/droid-configs.inc
