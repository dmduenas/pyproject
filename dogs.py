import requests
import json

dog_facts  = requests.get("https://dogapi.dog/api/v2/facts")

fact = dog_facts.json()["data"][0]["attributes"]["body"]

print(fact)