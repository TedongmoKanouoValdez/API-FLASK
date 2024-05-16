import requests

pikachu_data = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
pikachu_json=pikachu_data.json()
print(pikachu_json["name"])
