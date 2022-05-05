from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.jinja2')


@app.route('/tracks')
def tracks():
    return render_template('tracks.jinja2')


if __name__ == '__main__':
    app.run(debug=True)
