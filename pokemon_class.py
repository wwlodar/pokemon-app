import requests
from dictor import dictor

class Pokemon:
    def __init__(self, pname):
        self.pokemon_data = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(pname)).json()
        self.pokemon_number = int(dictor(self.pokemon_data, 'species.url')[42:].replace('/', ''))

    def pokemon_type(self):
        return dictor(self.pokemon_data, 'types.0.type.name'), dictor(self.pokemon_data, 'types.1.type.name')

    def pokemon_name(self):
        return dictor(self.pokemon_data, 'species.name')

    def pokemon_photo(self):
        return "https://pokeres.bastionbot.org/images/pokemon/" + str(self.pokemon_number) + str(".png")

    def pokemon_hp(self):
        return dictor(self.pokemon_data, 'stats.0.base_stat')

    def pokemon_attack(self):
        return dictor(self.pokemon_data, 'stats.1.base_stat')

    def pokemon_defense(self):
        return dictor(self.pokemon_data, 'stats.2.base_stat')

    def pokemon_speed(self):
        return dictor(self.pokemon_data, 'stats.5.base_stat')

    def pokemon_weak(self):
        url_weak = dictor(self.pokemon_data, 'types.0.type.url')
        url_weak = requests.get(url_weak)
        json_weak = url_weak.json()
        return dictor(json_weak, 'damage_relations.double_damage_from.0.name'), \
               dictor(json_weak, 'damage_relations.double_damage_from.1.name'), \
               dictor(json_weak, 'damage_relations.double_damage_from.2.name')

    def pokemon_strong(self):
        url_strong = dictor(self.pokemon_data, 'types.0.type.url')
        url_strong = requests.get(url_strong)
        json_strong = url_strong.json()
        return dictor(json_strong, 'damage_relations.double_damage_to.0.name'), \
               dictor(json_strong, 'damage_relations.double_damage_to.1.name')

