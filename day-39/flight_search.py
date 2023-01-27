import os
import requests


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    pass

# Constants
KIWI_ENDPOINT = "https://api.tequila.kiwi.com"
SEARCH_ENDPOINT = f"{KIWI_ENDPOINT}/v2/search"
SEARCH_API = os.environ.get("KIWI_API")
SEARCH_PARAMS = {
    "apikey": SEARCH_API,
    "fly_from": ,
    "fly_to:": ,
    "date_from": ,
    "date_to": ,
} # Note: Date format for this endpoint uses dd/mm/yyyy format
LOCATION_SEARCH_ENDPOINT = f"{KIWI_ENDPOINT}/locations/query"
LOCATION_PARAMS = {
    "apikey": SEARCH_API,
    "term": 
}


# Get the city rows
requests.get(url=)


# Lookup for the IATA Code


