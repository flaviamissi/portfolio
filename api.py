from flask import Flask, render_template
from site_info import site

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', page={}, site=site)

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)
