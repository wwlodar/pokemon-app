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

    def type1(self):
        if dictor(self.pokemon_data, 'types.1.type.name') == None:
            return dictor(self.pokemon_data, 'types.0.type.name')
        else:
           return dictor(self.pokemon_data, 'types.0.type.name'), dictor(self.pokemon_data, 'types.1.type.name')


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
