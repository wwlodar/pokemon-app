from flask import Flask, render_template, request
import requests
from dictor import dictor

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


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


@app.route('/pokemon')
def poke_name():
    pname = request.args.get('pname').lower()
    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(pname))
    if response.status_code == 200 and len(pname) != 0:
        response = response.json()
        chosen_pokemon = Pokemon(pname)
        return render_template('pokemon.html', pname=pname, chosen_pokemon=chosen_pokemon)
    elif response.status_code == 200 and len(pname) == 0:
        return render_template('home.html')
    else:
        return render_template('error.html', pname=pname)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
