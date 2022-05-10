from flask import Flask, render_template, url_for
from data import *

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def home():
    return render_template('home.jinja2')


@app.route('/tracks')
def tracks():
    return render_template('tracks.jinja2')


@app.route('/E1-Gokart')
def e1_gokart():
    sum_times = 0
    get_len_e1_gokart = len(e1_gokart_data)

    for i in range(0, get_len_e1_gokart):
        sum_times = sum_times + e1_gokart_data[i]

    average = round(sum_times / get_len_e1_gokart, 3)

    best_time = min(e1_gokart_data)

    return render_template('E1_Gokart.jinja2', average=average, best_time=best_time)


@app.route('/poznan-kart-track')
def poznan_kart_track():
    sum_times = 0
    get_len_poznan_kart_track = len(poznan_kart_track_data)

    for i in range(0, get_len_poznan_kart_track):
        sum_times = sum_times + poznan_kart_track_data[i]

    average = round(sum_times / get_len_poznan_kart_track, 3)

    best_time = min(bahrain_data)
    return render_template('Poznań_kart_track.jinja2', average=average, best_time=best_time)


@app.route('/bahrain')
def bahrain():
    sum_times = 0
    get_len_bahrain = len(bahrain_data)

    for i in range(0, get_len_bahrain):
        sum_times = sum_times + bahrain_data[i]

    average = round(sum_times / get_len_bahrain, 3)

    best_time = min(bahrain_data)
    return render_template('Bahrain.jinja2', average=average, best_time=best_time)


@app.route('/gallery')
def gallery():
    return render_template('gallery.jinja2')


@app.route('/about')
def about():
    return render_template('about.jinja2')


if __name__ == '__main__':
    app.run(debug=True)
