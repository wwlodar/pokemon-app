from flask import Flask, render_template, request
import requests
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/pokemon/<name>')
def poke_name():
    pname = request.args.get('pname')
    pname = pname.lower()
    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(pname))
    lower_letter = any(c.islower() for c in pname)
    return render_template('pokemon.html',pname=pname, lower = lower_letter, response=response)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
if __name__ == '__main__':
    app.run(debug = True)


