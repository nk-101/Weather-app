'''
import requests
import json

import win32com.client as wincom


city=input("Enter name of the city\n")
url = f'https://api.weatherapi.com/v1/current.json?key=3877ce43928244e59bd134238250101&q={city}'

r=requests.get(url)
#print(r.text)
#print(type(r.text))

wdic = json.loads(r.text)
w=wdic["current"]["temp_c"]

os.system(f"say 'the current weather in {city} is {w} degrees")
'''
import requests
import json
import win32com.client as wincom

# Initialize the text-to-speech engine
speaker = wincom.Dispatch("SAPI.SpVoice")

city = input("Enter the name of the city:\n")
url = f'https://api.weatherapi.com/v1/current.json?key=3877ce43928244e59bd134238250101&q={city}'

r = requests.get(url)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]

message = f"The current weather in {city} is {w} degrees Celsius."
print(message)
speaker.Speak(message)
