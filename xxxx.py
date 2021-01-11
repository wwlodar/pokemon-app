import requests
pname = "pikachu"
response = requests.get("https://pokeapi.co/api/v2/pokemon/"+ pname)
print(response)