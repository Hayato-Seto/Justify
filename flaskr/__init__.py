from . import calculate
from flask import Flask, render_template
import os

app = Flask(__name__, instance_relative_config=True)
app.secret_key = os.urandom(24)
# app.secret_key = "pACeg3URhtWCVwh7"


@app.route('/')
def hello():
    return render_template('home.html')


app.register_blueprint(calculate.bp)
