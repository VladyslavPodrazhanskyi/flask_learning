import json

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


with open('movies.json') as f:
    MOVIES = json.load(f)

print(len(MOVIES))

@app.route('/')
def home_page():
    return render_template('home.html', title='Home')


@app.route('/movies')
def movies_page():
    return render_template('movies.html', title='Movies list', movies=MOVIES)


@app.route('/<title>')
def movie_page(title):
    for i, movie in enumerate(MOVIES):
        if MOVIES[i].get('title') == title:
            return render_template('movie.html', title=title, movie=MOVIES[i])
    return redirect(url_for('movies_page'))
    # return render_template('movies.html', title='Movies list', movies=MOVIES)  # use redirect



@app.route('/test')
def test():
    massive = [
        {"a": 1, "b": 2, "c": 3},
        {"a": 12, "b": 21, "c": 31},
        {"a": 112, "b": 222, "c": 35},
        {"a": 122, "b": 23, "c": 345},
    ]
    return render_template('test.html', massive=enumerate(massive))

if __name__ == '__main__':
    app.run(debug=True)