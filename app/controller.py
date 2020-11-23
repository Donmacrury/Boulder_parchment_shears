from flask import render_template, request, redirect
from app import app

from app.models.player import Player

@app.route('/')
def index():
    return render_template("index.html", title='Home')

@app.route('/rock')
def player_1_rock():
    return render_template("rock.html", title='Rock')

@app.route('/scissors')
def player_1_scissors():
    return render_template("scissors.html", title='Scissors')

@app.route('/paper')
def player_1_paper():
    return render_template("paper.html", title='Paper')

@app.route('/rules')
def rules():
    return render_template("rules.html", title='Rules')

# @app.route('/rock/paper')
# def show_outcome():

#     game.players = Player()
#     return redirect('outcome.html', title='Outcome')