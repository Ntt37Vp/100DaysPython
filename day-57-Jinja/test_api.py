import requests

gender_url = "https://api.genderize.io/"
age_url = "https://api.agify.io/"
gender_param = {
    "name": "Kevin"
}

gender_response = requests.get(gender_url, params=gender_param)
gender = gender_response.json()["gender"]
print(gender)
