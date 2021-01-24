import requests
import json
from dictor import dictor
##pname = input("AFJDSJG")
##response = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(pname))
##todos = json.loads(response.text)
##anali = dictor(todos, 'types.0.type.name')
##print(todos)
##print(anali)

number = 42
response = requests.get("https://pokeres.bastionbot.org/images/pokemon/" + str(number) + str(".png"))
print(response.text)
