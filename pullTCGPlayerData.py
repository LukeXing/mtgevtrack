#note - tcgplayer is currently not granting keys at this time

import requests
import json
import access_tokens_tcg as tokens

# Set your TCGplayer API access token here
ACCESS_TOKEN = tokens.tcg_player_access_token

# Set the endpoint URL for getting Magic the Gathering sets
SET_ENDPOINT = "https://api.tcgplayer.com/catalog/categories/1/search"

# Set the parameters for the API request
params = {
    "sort": "releaseDate desc",
    "limit": 100,
    "categoryId": 1,
    "productTypes": "Magic Booster",
    "getExtendedFields": True
}

# Set the authorization headers
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Accept": "application/json"
}

# Make the API request and parse the response
response = requests.get(SET_ENDPOINT, params=params, headers=headers)
data = json.loads(response.content.decode())

# Print the names and release dates of the Magic the Gathering sets
for set_data in data["results"]:
    set_name = set_data["name"]
    release_date = set_data["extendedData"]["ReleaseDate"]
    print(f"{set_name}: {release_date}")