import requests
import json


user_choice = input("Pick a band name: ")
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + user_choice)


print(json.dumps(response.json(), indent=2))