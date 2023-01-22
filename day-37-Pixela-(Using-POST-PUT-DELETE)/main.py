import requests
from datetime import datetime


# Creating a user (POST)
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_USERNAME = "huntertrump"
PIXELA_TOKEN = "btTeo4TnJ4tvXoNSE4"
USER_PARAMETERS = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=PIXELA_ENDPOINT, json=USER_PARAMETERS)
# print(response.text)
# success!


# Creating a graph (POST)
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"
GRAPH_CONFIG = {
    "id":"graph3",
    "name":"Coding-Marathon",
    "unit":"hours",
    "type":"float",
    "color":"shibafu",
    "timezone":"Asia/Singapore",
}
HEADERS = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}
# response = requests.post(url=GRAPH_ENDPOINT, json=GRAPH_CONFIG, headers=HEADERS)
# print(response.text)
# success!
# to view in browser https://pixe.la/v1/users/huntertrump/graphs/graph3.html


today = datetime.now()
PLOT_ENDPOINT = f"{GRAPH_ENDPOINT}/graph3"
PLOT_PARAM = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "0",
}
# response = requests.post(url=PLOT_ENDPOINT, json=PLOT_PARAM, headers=HEADERS)
# print(response.text)
# print(response.status_code)


# Using PUT to update an entry
DATE_TO_CORRECT = "20230122"
CORRECTION_ENDPOINT= f"{PLOT_ENDPOINT}/{DATE_TO_CORRECT}"
CORRECTION_PARAM = {
    "quantity":"2",
}
# response = requests.put(url=CORRECTION_ENDPOINT, json=CORRECTION_PARAM, headers=HEADERS)
# print(response.status_code)
# print(response.text)


# Using DELETE to remove an entry
DATE_TO_DELETE = "20230121"
DELETE_ENDPOINT = f"{PLOT_ENDPOINT}/{DATE_TO_DELETE}"
# response = requests.delete(url=DELETE_ENDPOINT, headers=HEADERS)
# print(response.status_code)
# print(response.text)
