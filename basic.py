from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

## work on adding more pokemons
@app.route('/pokemon')
def poke_name():
    pokemon_name = request.args.get('pname')
    lower_letter = any(c.islower() for c in pokemon_name)
    return render_template('pokemon.html',pokemon_name=pokemon_name, lower = lower_letter)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
if __name__ == '__main__':
    app.run(debug = True)
##base
