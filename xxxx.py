import requests

response = requests.get('https://pokeapi.co/api/v2/pokemon/' + str('pikachu'))
pokemon_data = response.json()
x = (pokemon_data['abilities'])
for ability in x:
    print(ability)
dict_pokemon = [{key : value} for (key, value) in x.items() ]
print(x)