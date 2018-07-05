## PythonHotspot

### Problem

When you have a device that requires a wireless connection but you do not 
know the WiFi details where it is going to be installed, you then require 
to mess around with configuration files, on site.

### Solution

Have a WiFi hotspot start when you power on the device which has a web page 
allowing you to select from a list of Wifi networks within range, 
or specify a hidden network.

Then save the conenction for future boots, and allow the user to change 
network by accessing the web page, or moving the device outside the range 
of the existing network, and the hotspot will start back up again.

NOTE:
This is currently set up to run the hotspot when ever there is no network 
connectivity, so if the device is running on ethernet, it will not start the hotspot.


### So far

I have attempted to use the resin-wifi-connect, and this works fantastically, 
excpet I do now know Rust, and it also does not persist the 'saved' connection 
across boots.

I know more about Python, and also prefer the ability to test sections of code, 
and open up functions whilst running the code, and not have to re-compile it.

That being said, to be able to compile the code, would be very helpful, 
in not having to have additional dependents on the system.

### License

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

### TODO

 * Built the web page
 * Design the web page
 * Pipify the program/module
 * Create automated tests
 * Confirm it works in Docker, with Resin
