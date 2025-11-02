import requests
from datetime import datetime

current_time = datetime.now()
api_key = "9a311fd6832dca1fc646b098cb3bd10b"

user_input = input("Enter City: ").capitalize()

weather_call = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

sky = weather_call.json()["weather"][0]["description"]
temperature = weather_call.json()["main"]["temp"]
wind_speed = weather_call.json()["wind"]["speed"]

print(f"\nLocation: {user_input}")
print(f"As of {current_time}")
print(f"The sky will be {sky}")
print(f"The temperature is {temperature}")
print(f"The wind speeds are {wind_speed}\n")
