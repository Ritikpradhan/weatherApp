import os
import requests
import json
import pyttsx3
from datetime import datetime


city = input("Enter the  city name\n")

url= f"https://api.weatherapi.com/v1/current.json?key=b6e3da6e844444e3b8c110954230708&q={city}"

r = requests.get(url)
print(r.text)
wdic = json.loads(r.text)
w =wdic["current"]["temp_c"]
feels_like = wdic["current"]["feelslike_c"]
humidity = wdic["current"]["humidity"]
cloud = wdic["current"]["cloud"]
winds = wdic["current"]["wind_kph"]
wind_dir = wdic["current"]["wind_dir"]
current_time = datetime.now().strftime("%H:%M")


engine = pyttsx3.init()
engine.say(f"The current weather in {city} at {current_time} is {w} degree")
engine.say(f"It feels like {feels_like} degrees celsius.")
engine.say(f"The humidity is {humidity}% in the air")
engine.say(f"The cloud coverage is {cloud}%")
engine.say(f"The wind is at the speed of {winds} km per hours")
engine.say(f"And the direction of wind is {wind_dir} direction.")
engine.runAndWait()