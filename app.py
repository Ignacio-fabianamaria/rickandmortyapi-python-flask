from flask import Flask, render_template, request
import urllib.request, json

app = Flask(__name__)

# flask --app app run


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/characters")
def get_list_characters_page():
    page = request.args.get("page", 1, type=int)
    url = f"https://rickandmortyapi.com/api/character/?page={page}"
    response = urllib.request.urlopen(url)
    data = response.read()
    character_data = json.loads(data)
    return render_template(
        "characters.html",
        characters=character_data["results"],
        info=character_data["info"],
        current_page=page,
    )


@app.route("/profile/<id>")
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return render_template("profile.html", profile=dict)


@app.route("/episodes")
def get_list_episodes_page():
    page = request.args.get("page", 1, type=int)
    url = f"https://rickandmortyapi.com/api/episode/?page={page}"
    response = urllib.request.urlopen(url)
    data = response.read()
    episodes_data = json.loads(data)
    return render_template(
        "episodes.html",
        episodes=episodes_data["results"],
        info=episodes_data["info"],
        current_page=page,
    )


@app.route("/episode/<id>")
def get_episode(id):
    url = f"https://rickandmortyapi.com/api/episode/{id}"
    response = urllib.request.urlopen(url)
    data = response.read()
    episode_data = json.loads(data)

    characters = []
    for character_url in episode_data.get('characters', []):
        character_response = urllib.request.urlopen(character_url)
        character_data = json.loads(character_response.read())
        characters.append(character_data)

    return render_template('episode.html', episode=episode_data, characters=characters)
