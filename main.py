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

from flask import Flask, request, render_template

import dev as nm

import subprocess
app = Flask(__name__)

def get_essids():
    essids=nm.get_ssids()
    return essids


def show_settings():
    pass
    return render_template('settings.html',title='Settings', essids=get_essids())

def save_settings():
    essid = request.form['essid']
    psk = request.form['psk']

    nm.remove_connection(ssid)
    nm.create_connection(essid,psk)

    return render_template('saved.html', title='Saved')



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return save_settings()
    else:
        return show_settings()


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
