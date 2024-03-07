import requests



url = "https://pokeapi.co/api/v2/pokemon?limit=386"

response = requests.get(url=url)

pokemon = response.json()

print(pokemon)
