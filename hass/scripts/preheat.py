import requests
import json
import sys, time
import simplejson

MODE, PREHEAT_BED_TEMP, PREHEAT_TOOL_TEMP, FAN_SPEED = sys.argv[1:5]



API_KEY = "6110A9B9D7034C6B9CB1EC041C4BBAE0"
BASE_URL = "http://localhost:5000"


#turn on printer

#is the printer on (does ttyUSB exist?)

#connect to the printer

#preheat printer

def available_ports():
	j = requests.get(BASE_URL+"/api/connection", headers={"X-Api-Key":API_KEY}).json()
	return j["options"]["ports"]

def is_printer_on(ports):
	for port in ports:
		if port.startswith("/dev/ttyUSB"):
			return port
	return False

def is_connected():
	j = requests.get(BASE_URL+"/api/connection", headers={"X-Api-Key":API_KEY}).json()
	return j["current"]["state"] != "Closed" and not j["current"]["port"] == None

def get_preferred_port():
	j = requests.get(BASE_URL+"/api/connection", headers={"X-Api-Key":API_KEY}).json()
	return j["options"]["portPreference"]

def connect():
	j = requests.post(BASE_URL+"/api/connection", json={"command":"connect"}, headers={"X-Api-Key":API_KEY})

def preheat():
	commands = ["M104 S"+PREHEAT_TOOL_TEMP,
				"M140 S"+PREHEAT_BED_TEMP,
				"M106 S"+FAN_SPEED]
	print(commands)
	j = requests.post(BASE_URL+"/api/printer/command", json={"commands":commands}, headers={"X-Api-Key":API_KEY})

def zero_temp():
	commands = ["M104 S0",
				"M140 S0",
				"M106 S0"]
	print(commands)
	j = requests.post(BASE_URL+"/api/printer/command", json={"commands":commands}, headers={"X-Api-Key":API_KEY})

def preheat_on():
	try:
		j = requests.get(BASE_URL+"/api/printer", headers={"X-Api-Key":API_KEY}).json()
		return float(j["temperature"]["bed"]["target"]) > 0 or float(j["temperature"]["tool0"]["target"]) > 0
	except simplejson.errors.JSONDecodeError:
		return False



if MODE == "on":
	ports = available_ports()
	printer_state = is_printer_on(ports)
	if not printer_state:
		pass
		#printer not on, do nothing, maybe wait 10 seconds and try again
	else:
		connected = is_connected()
		if connected:
			preheat()
		else:
			connect()
			time.sleep(30)
			preheat()
elif MODE == "off":
	zero_temp()
elif MODE == "state":
	ph = preheat_on()
	if ph:
		print("ON")
	else:
		print("OFF")
