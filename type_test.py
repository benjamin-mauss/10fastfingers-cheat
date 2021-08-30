import requests
from time import time

import urllib3
import json

urllib3.disable_warnings()

f = open("config.json")
config = json.load(f)
f.close()

ts = int(time())*1000 # milisecond
tsf = ts + 60024 # timestamp final


user_input = ""
wpm = config["wpm"]

words = config["wordlist"].split("|")

if  wpm > len(words): 
    wpm = len(words)
    print("#### limit of WPM excided, setting to the max ####")

for c in range(0, wpm):
    user_input += words[c] + " "


burp0_data = {"sz": ts, "ez": tsf, "wordlist": config["wordlist"], "user_input": user_input, "backspace_counter": "0", "afk_timer": "1", "speedtest_id": "1", "mode": "advanced"}

requests.post("https://10fastfingers.com/speedtests/auswertung", headers=config["burp0_headers"], cookies=config["burp0_cookies"], data=burp0_data, proxies=config["burp0_proxy"], verify=False)

