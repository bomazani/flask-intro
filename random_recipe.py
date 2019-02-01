from flask import Flask
from flask import render_template
from tinydb import TinyDB, Query
import random

app = Flask(__name__)
db = TinyDB('db.json')

@app.route('/')
def random_recipe():
    recipe = random.choice(db.all())
    return render_template('recipe.html', recipe=recipe)
