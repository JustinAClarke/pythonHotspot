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
