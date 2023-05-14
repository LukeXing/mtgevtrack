import requests


def getMostRecentSetsData():
    # pulls most recent sets info into a json file called sets

    url = "https://deckmaster.info/sets.php?format=json"
    filename = "sets.json"

    response = requests.get(url)

    if response.status_code == 200:
        with open(filename, 'w') as f:
            f.write(response.text)
            print(f"Successfully saved JSON data to {filename}")
    else:
        print(f"Error downloading JSON data: {response.status_code}")
