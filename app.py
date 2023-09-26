from flask import Flask, render_template, jsonify
from Data.pictures import pictures
import random

app = Flask(__name__)

# Page d'accueil
@app.route('/')
def home():
    return render_template('home.html')


# Liste des images
@app.route('/api/pictures')
def picture_list():
    return render_template('home.html', pictures=pictures)

# API pour obtenir la liste de tous les films
@app.route('/api/pictures')
def api_picture_list():
    return render_template("pictures.py")

# API pour obtenir la liste de tous les films
@app.route('/api/pictures/shuffle')
def shulffle():
    random.shuffle(pictures)
    return render_template("shuffle.html", pictures=pictures )


# API pour obtenir un film par ID
@app.route('/api/picture/<int:id>')
def api_picture(id):
    picture = next((p for p in pictures if p["id"] == id), None)
    if picture:
        return render_template("pictures.html", picture=picture)
    else:
        return "Image non trouvée", 404


if __name__ == '__main__':
    app.run(debug=True)