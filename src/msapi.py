import requests
import json

class Client:

	def __init__(self, address:str):
		self.api     = "https://api.mcsrvstat.us/";
		self.address = address;
		self.res     = requests.get(f"{self.api}2/{address}").json();

		if self.res["ip"] == "":
			self.res = None;

		self.online  = self.res["online"];

	def get_data_server(self):
		return self.res;

	def icon_server(self):
		return requests.get(f"{self.api}icon/{self.address}").content

	def debug_server(self):
		return self.res["debug"];

	def motd_server(self):
		return self.res["motd"];

	def players_server(self):
		return requests.get(f"https://api.mcsrvstat.us/ping/{self.address}").json()["players"];

	def plugins_server(self):
		if "plugins" not in self.res:
			return None;

		return self.res["plugins"]["raw"];