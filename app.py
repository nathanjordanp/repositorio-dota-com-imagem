from flask import Flask, render_template
from objeto import Heroes


hero_list = [Heroes(1, 'Dark Willow', 'support', 'nuking support that helps the mid game better', 'darkwillow.jpeg'),
              Heroes(2, 'Marci', 'Melee hero that can be played as either roles', 'strong ultimate but kitable', 'marci.jpeg'),
              Heroes(3, 'Bane', 'Support', 'Lots of disables and ganking potantial but low range in lane', 'bane.jpeg')
]


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", hero_list = hero_list)

@app.route("/dota/<int:id>")
def dotinha(id):
    for objeto in hero_list:
        if objeto.get_id() == id:
            return render_template("dota.html", objeto = objeto)