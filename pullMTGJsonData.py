import requests
import json

# Set the endpoint URL for getting the price data
SET_CODE = 
PRICE_ENDPOINT = "https://api.scryfall.com/cards/search?q=set:sta"

# Make the API request and parse the response
try:
    response = requests.get(PRICE_ENDPOINT)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    exit(1)
except json.JSONDecodeError as e:
    print(f"Error: Unable to decode JSON response. {e}")
    exit(1)

# Get the prices for each card in the set
prices = {}
for card in data["data"]:
    card_name = card["name"]
    card_price = card["prices"]["usd"]
    prices[card_name] = card_price

# Print the prices for each card in the set
print("Prices for Strixhaven: Mystical Archive:")
for card_name, card_price in prices.items():
    print(f"{card_name}: ${card_price}")