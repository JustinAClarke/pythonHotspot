"""    
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
"""

from time import sleep

from flask import Flask, request, render_template, jsonify

import dev as nm

app = Flask(__name__)

SSID = "pyHotspot"
PSK = "P@s5w0rd!"

def get_essids():
    essids=nm.get_ssids()
    return essids


def show_settings():
    pass
    return render_template('settings.html',title='Settings', essids=get_essids())

def save_settings():
    essid = request.form['essid']
    psk = request.form['psk']

    nm.create_connection(essid,psk)
    nm.remove_connection(SSID)

    return render_template('saved.html', title='Saved')



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return save_settings()
    else:
        return show_settings()

@app.route('/refresh', methods=['GET'])
def refresh():
    ssids=nm.get_ssids()
    return jsonify(ssids)

if __name__ == "__main__":
    if not nm.is_connected():
        print("No Network starting hotspot")
        #Networking failed, run hotspot
        nm.deactivate_connections()
        sleep(5)
        print(nm.get_ssids())
        hotspot_startup = nm.activate_hotspot(SSID,PSK)
    else:
        print("Network Connected, not doing anything")

    #either way start web page
    app.run(host='0.0.0.0')
