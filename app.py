from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)

# flask --app app run


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/characters")
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return render_template("characters.html", characters=dict["results"])


@app.route("/profile/<id>")
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return render_template("profile.html", profile=dict)


@app.route("/lista")
def get_list_elements():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    characters = response.read()
    data = json.loads(characters)

    characters = []

    for character in data["results"]:
        character = {"name": character["name"], "status": character["status"]}
        characters.append(character)
    return {"characters": characters}

