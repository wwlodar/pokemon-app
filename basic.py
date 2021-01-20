from flask import Flask, render_template, request
import requests

from dictor import dictor
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

def reading_pokemon_data():
    global anali
    global response
    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(pname))
    pokemon_data = response.json()
    anali = dictor(pokemon_data, 'types.0.type.name')


@app.route('/pokemon')
def poke_name():
    global pname
    pname = request.args.get('pname').lower()
    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(pname))
    if response.status_code == 200 and len(pname) != 0:
        reading_pokemon_data()
        return render_template('pokemon.html', pname=pname, anali=anali)
    elif response.status_code == 200 and len(pname) == 0:
        return render_template('home.html')
    else:
        return render_template('error.html', pname=pname)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
