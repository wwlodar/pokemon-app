import requests
import json
from dictor import dictor
##pname = input("AFJDSJG")
##response = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(pname))
##todos = json.loads(response.text)
##anali = dictor(todos, 'types.0.type.name')
##print(todos)
##print(anali)

class Pokemon():
    def __init__(self, pname):
        self.pokemon_data =  requests.get('https://pokeapi.co/api/v2/pokemon/' + str(pname)).json()

    def typeee(self):
        return dictor(self.pokemon_data, 'types.1')

p = Pokemon("nidoqueen")
print(p.typeee())