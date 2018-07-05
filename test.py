'''
import dbus
bus = dbus.SystemBus()
proxy = bus.get_object("org.freedesktop.NetworkManager", "/org/freedesktop/NetworkManager/Settings")
settings = dbus.Interface(proxy, "org.freedesktop.NetworkManager.Settings")

'''

'''import dbus

def test(obj):
    bus = dbus.SystemBus()
    proxy = bus.get_object("org.freedesktop.NetworkManager", "/"+obj.replace('.','/'))
    interface = dbus.Interface(proxy, obj)
    return interface
'''

"""
Display all visible SSIDs
"""

import NetworkManager

for dev in NetworkManager.NetworkManager.GetDevices():
    if dev.DeviceType != NetworkManager.NM_DEVICE_TYPE_WIFI:
        continue
    for ap in dev.GetAccessPoints():
        print('%-30s %dMHz %d%%' % (ap.Ssid, ap.Frequency, ap.Strength))
