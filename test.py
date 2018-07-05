'''
    PythonHotspot Justin Fuhrmeister-Clarke, a python and web based networking setup system.
    Copyright (C) 2018  Justin Fuhrmeiser-Clarke <justin@fuhrmeister-clarke.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
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
