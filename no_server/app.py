from flask import Flask, render_template
import json
from .main import plot
from bokeh.embed import json_item


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/figure')
def figure():
    return json.dumps(json_item(plot()))
