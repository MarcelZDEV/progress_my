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


@app.route('/gallery')
def gallery():
    return render_template('gallery.jinja2')


if __name__ == '__main__':
    app.run(debug=True)
