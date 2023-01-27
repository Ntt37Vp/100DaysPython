import os
import requests


SHEET_ENDPOINT = "https://api.sheety.co/d058581b665d834a29813c71c35e3681/flightDeals/prices"
SHEET_AUTH = os.environ.get("SHEET_PRICE_AUTH")
SHEET_HEADER = {
    "Authorization": SHEET_AUTH
}
DATA_TO_PARSE = {
    "price": {
        "city": ,
        "iataCode": ,
        "lowestPrice": ,
    }
}

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    pass



