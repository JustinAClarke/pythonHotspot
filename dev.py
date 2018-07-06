import NetworkManager
import uuid

SSID='resin'
PSK='resintest'

def create_connection(ssid,psk,hotspot=False):
    mode='infrastructure'
    ip_setting='auto'
    if hotspot:
        mode='ap'
        ip_setting='shared'
    hotspot = {
         '802-11-wireless': {'mode': mode,
                             'security': '802-11-wireless-security',
                             'ssid': ssid},
         '802-11-wireless-security': {'auth-alg': 'open', 'key-mgmt': 'wpa-psk', 'psk': psk},
         'connection': {'id': ssid,
                        'type': '802-11-wireless',
                        'uuid': str(uuid.uuid4())},
         'ipv4': {'method': ip_setting},
         'ipv6': {'method': ip_setting}
    }

    return NetworkManager.Settings.AddConnection(hotspot)


def get_hotspot(ssid,psk):
    #check if hotspot/connection exists
    #NetworkManager.Settings.Connections[0].GetSettings()['connection']['id']
    for connection in NetworkManager.Settings.Connections:
        if connection.GetSettings()['connection']['id'] == ssid:
            return connection
        else:
            return create_connection(ssid,psk,True)

def activate_hotspot(ssid,psk):
    conn = get_hotspot(ssid,psk)
    # Find a suitable device
    ctype = conn.GetSettings()['connection']['type']
    if ctype == 'vpn':
        for dev in NetworkManager.NetworkManager.GetDevices():
            if dev.State == NetworkManager.NM_DEVICE_STATE_ACTIVATED and dev.Managed:
                break
        else:
            raise Exception("No active, managed device found")
            
    else:
        dtype = {
            '802-11-wireless': NetworkManager.NM_DEVICE_TYPE_WIFI,
            '802-3-ethernet': NetworkManager.NM_DEVICE_TYPE_ETHERNET,
            'gsm': NetworkManager.NM_DEVICE_TYPE_MODEM,
        }.get(ctype,ctype)
        devices = NetworkManager.NetworkManager.GetDevices()

        for dev in devices:
            if dev.DeviceType == dtype and dev.State == NetworkManager.NM_DEVICE_STATE_DISCONNECTED:
                break
        else:
            raise Exception("No suitable and available %s device found" % ctype)
            

    # And connect
    return NetworkManager.NetworkManager.ActivateConnection(conn, dev, "/")

def remove_connection(ssid):
    for connection in NetworkManager.Settings.Connections:
        if connection.GetSettings()['connection']['id'] == ssid:
            print(connection)
            connection.Delete()

def get_ssids():
    ssids=[]
    for dev in NetworkManager.NetworkManager.GetDevices():
        if dev.DeviceType != NetworkManager.NM_DEVICE_TYPE_WIFI:
            continue
        for ap in dev.GetAccessPoints():
            ssids.append({'essid':ap.Ssid,'freq':ap.Frequency,'strength':ap.Strength})
    return ssids

if __name__ == "__main__":
    if NetworkManager.NetworkManager.Connectivity != 4:
        print("No Network starting hotspot")
        #Networking failed, run hotspot
        for active in NetworkManager.NetworkManager.ActiveConnections:
            NetworkManager.NetworkManager.DeactivateConnection(active)
        hotspot_startup = activate_hotspot(SSID,PSK)
    else:
        print("Network Connected, not doing anything")
        
