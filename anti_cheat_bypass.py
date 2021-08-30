import requests 
import easyocr 
import shutil 
import time

### configurations

import urllib3
import json
  
urllib3.disable_warnings()

f = open("config.json")
config = json.load(f)
f.close()

### downloading the image

burp1_url = "https://10fastfingers.com:443/anticheat/generate_word_picture?rand=4640736981"

response = requests.get(burp1_url, stream=True, headers=config["burp0_headers"], cookies=config["burp0_cookies"], proxies=config["burp0_proxy"], verify=False)

### saving the image to a file

file = open("resp.png", "wb")
response.raw.decode_content = True
shutil.copyfileobj(response.raw, file)        
file.close()

### understand the image's text

reader = easyocr.Reader(['en'], gpu=True)
obj_text = reader.readtext("./resp.png")
from os import system
system("clear")
final_text = ""
for obj_text2 in obj_text:
    if len(str(obj_text2[1])) > 10: # this line can be removed :)
        final_text += obj_text2[1] + ' '
print(final_text)

### avoid detection
time.sleep(3)

### sending to the anti cheat :)
burp0_data = {"eingabe_string": final_text, "backspace_counter": "0"}
requests.post("https://10fastfingers.com:443/anticheat/auswertung_anticheat", headers=config["burp0_headers"], cookies=config["burp0_cookies"], data=burp0_data, proxies=config["burp0_proxy"], verify=False)

