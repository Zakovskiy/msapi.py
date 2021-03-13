# example save_icon.py
# https://github.com/Zakovskiy/msapi.py

import msapi;

MS = msapi.Client("address");

r = MS.icon_server();

f = open("./icon.jpg", "wb");
f.write(r);
f.close();