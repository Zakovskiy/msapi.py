# example plugins.py
# https://github.com/Zakovskiy/msapi.py

import msapi

MS = msapi.Client("address");

plugins = MS.plugins_server();

if not plugins:
	exit("Error >> This server hide plugins");

for i in plugins:
	print(i);