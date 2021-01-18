from flask import Flask, render_template, request
import requests
import json
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

def get_pokemon():
    global pname
    pname = request.args.get('pname')
    pname = pname.lower()
    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(pname))
    global pokemon_data
    pokemon_data = response.json()
    global ability
    ability = pokemon_data['abilities']
    global lower_letter
    lower_letter = any(c.islower() for c in pname)


@app.route('/pokemon')
def poke_name():
    get_pokemon()
    type = pokemon_data['types']
    return render_template('pokemon.html', pname=pname, lower=lower_letter, ability=ability,type=type)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
if __name__ == '__main__':
    app.run(debug = True)
##base
