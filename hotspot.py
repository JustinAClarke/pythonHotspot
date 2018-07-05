''' python-networkmanager example'''

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

"""
Add a connection to NetworkManager. You do this by sending a dict to
AddConnection. The dict below was generated with n-m dump on an existing
connection and then anonymised
"""

import NetworkManager
import uuid

hotspot = {
     '802-11-wireless': {'mode': 'ap',
                         'security': '802-11-wireless-security',
                         'ssid': 'n-m-example-connection'},
     '802-11-wireless-security': {'auth-alg': 'open', 'key-mgmt': 'wpa-psk', 'psk': 'resin_hotspot'},
     'connection': {'id': 'nm-example-connection',
                    'type': '802-11-wireless',
                    'uuid': str(uuid.uuid4())},
     'ipv4': {'method': 'shared'},
     'ipv6': {'method': 'shared'}
}

print(NetworkManager.Settings.AddConnection(hotspot))
