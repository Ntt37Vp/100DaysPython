import requests


# Ask user input
exercises = input("Tell me the exercises you did ")

# Constants
ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
PARAMS = {
    "query": exercises,
}
HEADERS = {
    "x-app-id": "f6026853",
    "x-app-key": "a7c20eada91d6bebd28948b3317e004e",
}

response = requests.post(url=ENDPOINT, json=PARAMS, headers=HEADERS)
result = response.json()
print(result)
