from flask import Flask, render_template, url_for, request
from data import *
import datetime

app = Flask(__name__, static_url_path='/static')
target_time_delta = 0.005


@app.route('/')
def home():
    return render_template('templates/home.jinja2')


@app.route('/tracks')
def tracks():
    return render_template('templates/tracks.jinja2')


@app.route('/E1-Gokart')
def e1_gokart():
    # global variables for this function

    get_len_e1_gokart = 1
    vehicle_input_e1_gokart = e1_gokart_data

    # sum all numbers from list
    sum_numbers_poznan_kart_track = sum(vehicle_input_e1_gokart)

    # average from all numbers in list
    average_e1_gokart = round(sum_numbers_poznan_kart_track / get_len_e1_gokart, 3)

    # get the lowest number to know what is the best time
    best_time_e1_gokart = min(vehicle_input_e1_gokart)

    return render_template('templates/E1_Gokart.jinja2', average=average_e1_gokart, best_time=best_time_e1_gokart)


@app.route('/poznan-kart-track', methods=['POST', 'GET'])
def poznan_kart_track():
    # global variables for this function

    # variables for e sport
    average_poznan_kart_track = 0
    best_time_poznan_kart_track = 0
    vehicle_input_poznan_kart_track = []
    vehicle_poznan_kart_track = ''
    target_time = 0
    get_len_poznan_kart_track = 1

    # variables for on track
    average_poznan_kart_track_ontrack = 0
    best_time_poznan_kart_track_ontrack = 0
    target_time_ontrack = 0

    # check do request is post
    if request.method == 'POST':
        # get vehicle from dropdown
        vehicle_poznan_kart_track = request.form['cars']

        if vehicle_poznan_kart_track == 'Kart 125':
            # set values for variables
            vehicle_input_poznan_kart_track = poznan_kart_track_data_kart_125
            get_len_poznan_kart_track = len(poznan_kart_track_data_kart_125)
        elif vehicle_poznan_kart_track == 'Kart 50':
            # set values for variables
            vehicle_input_poznan_kart_track = poznan_kart_track_data_kart_50
            get_len_poznan_kart_track = len(poznan_kart_track_data_kart_50)

        # times e-sport

        # sum all numbers from list
        sum_numbers_poznan_kart_track = sum(vehicle_input_poznan_kart_track)

        # average from all numbers in list
        average_poznan_kart_track = round(sum_numbers_poznan_kart_track / get_len_poznan_kart_track, 3)

        # get the lowest number to know what is the best time
        best_time_poznan_kart_track = min(vehicle_input_poznan_kart_track)

        # target time e-sport
        target_time = best_time_poznan_kart_track - target_time_delta

        # times on track

        # get len of list
        get_len_poznan_kart_track_ontrack = len(poznan_kart_kart_track_data)

        # sum all numbers from list
        sum_numbers_poznan_kart_track_ontrack = sum(poznan_kart_kart_track_data)

        # get the lowest number to know what is the best time
        best_time_poznan_kart_track_ontrack = min(poznan_kart_kart_track_data)

        # average from all numbers in list
        average_poznan_kart_track_ontrack = round(sum_numbers_poznan_kart_track_ontrack / get_len_poznan_kart_track_ontrack)

        # target time on track
        target_time_ontrack = best_time_poznan_kart_track_ontrack = target_time_delta

    return render_template('templates/Pozna??_kart_track.jinja2', average=average_poznan_kart_track,
                           best_time=best_time_poznan_kart_track, vehicle=vehicle_poznan_kart_track, target=target_time, average_ontrack=average_poznan_kart_track_ontrack, best_time_ontrack=best_time_poznan_kart_track_ontrack, target_time_ontrack=target_time_ontrack)


@app.route('/bahrain', methods=['POST', 'GET'])
def bahrain():
    average_bahrain = 0
    best_time_bahrain = 0
    vehicle_input_bahrain = []
    vehicle_bahrain = ''
    target_time = 0

    if request.method == 'POST':
        vehicle_bahrain = request.form['cars']
        get_len_bahrain = 1

        if vehicle_bahrain == 'F1 2021 formula':
            vehicle_input_bahrain = bahrain_data_f1_2021
            get_len_bahrain = len(bahrain_data_f1_2021)

        sum_numbers_bahrain = sum(vehicle_input_bahrain)

        average_bahrain = sum_numbers_bahrain / get_len_bahrain
        average_bahrain = round(average_bahrain / 60, 3)

        best_time_bahrain = min(vehicle_input_bahrain)
        best_time_bahrain = round(best_time_bahrain / 60, 3)

        target_time = round(best_time_bahrain - target_time_delta, 3)
    return render_template('templates/Bahrain.jinja2', average=average_bahrain, best_time=best_time_bahrain, vehicle=vehicle_bahrain, target=target_time)


@app.route('/imola', methods=['POST', 'GET'])
def imola():
    # global variables for this function

    # variables for e sport
    average_imola = 0
    best_time_imola = 0
    vehicle_input_imola = []
    vehicle_imola = ''
    target_time = 0
    get_len_imola = 1

    # check do request is post
    if request.method == 'POST':
        # get vehicle from dropdown
        vehicle_imola = request.form['cars']

        if vehicle_imola == 'F1 2021 formula':
            # set values for variables
            vehicle_input_imola = imola_data_f1_2021
            get_len_imola = len(imola_data_f1_2021)

        # times e-sport

        # sum all numbers from list
        sum_numbers_poznan_kart_track = sum(vehicle_input_imola)

        # average from all numbers in list
        average_poznan_kart_track = round(sum_numbers_poznan_kart_track / get_len_imola, 3)

        # get the lowest number to know what is the best time
        best_time_poznan_kart_track = min(vehicle_input_imola)

        # target time e-sport
        target_time = best_time_poznan_kart_track - target_time_delta

    return render_template('templates/Imola.jinja2', average=average_imola,
                           best_time=best_time_imola, vehicle=vehicle_imola, target=target_time, )


@app.route('/singapore', methods=['POST', 'GET'])
def singapore():
    average_singapore = 0
    best_time_singapore = 0
    vehicle_input_singapore = []
    vehicle_singapore = ''
    target_time = 0

    if request.method == 'POST':
        vehicle_singapore = request.form['cars']
        get_len_singapore = 1

        if vehicle_singapore == 'F1 2021 formula':
            vehicle_input_singapore = singapore_data_f1_2021
            get_len_singapore = len(singapore_data_f1_2021)

        sum_numbers_singapore = sum(vehicle_input_singapore)

        average_singapore = round(sum_numbers_singapore / get_len_singapore, 3)

        best_time_singapore = min(vehicle_input_singapore)

        target_time = best_time_singapore - target_time_delta
    return render_template('templates/Singapore.jinja2', average=average_singapore, best_time=best_time_singapore, target=target_time, vehicle=vehicle_singapore)


@app.route('/nurburgring', methods=['POST', 'GET'])
def nurburgring():
    average_nurburgring = 0
    best_time_nurburgring = 0
    vehicle_input_nurburgring = []
    vehicle_nurburgring = ''
    target_time = 0

    if request.method == 'POST':
        vehicle_nurburgring = request.form['cars']
        get_len_nurburgring = 1

        if vehicle_nurburgring == 'Porsche 911 gt3 R':
            vehicle_input_nurburgring = nurburgring_data_porsche_911_gt3_r
            get_len_nurburgring = len(nurburgring_data_porsche_911_gt3_r)

        sum_numbers_nurburgring = sum(vehicle_input_nurburgring)

        average_nurburgring = round(sum_numbers_nurburgring / get_len_nurburgring)
        average_nurburgring = datetime.timedelta(seconds=average_nurburgring)

        best_time_nurburgring = min(vehicle_input_nurburgring)
        best_time_nurburgring = round(best_time_nurburgring)
        best_time_nurburgring = datetime.timedelta(seconds=best_time_nurburgring)

        target_time = best_time_nurburgring - target_time_delta
    return render_template('templates/N??rburgring.jinja2', average=average_nurburgring,
                           best_time=best_time_nurburgring, vehicle=vehicle_nurburgring, target=target_time)


@app.route('/gallery')
def gallery():
    return render_template('templates/gallery.jinja2')


@app.route('/about')
def about():
    return render_template('templates/about.jinja2')


if __name__ == '__main__':
    app.run(debug=True)
