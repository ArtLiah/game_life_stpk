from flask import Flask, render_template
import game_of_life

app = Flask(__name__)


@app.route('/')
def index():
    game_of_life.GameOfLife(10, 10)
    return render_template('index.html', )


@app.route('/live')
def live():
    game = game_of_life.GameOfLife()
    game.form_new_generation()
    game_of_life.counter = +1
    return render_template('live.html', game=game, counter=game_of_life.counter)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
