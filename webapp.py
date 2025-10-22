from flask import Flask, url_for, render_template, request

import json

app = Flask(__name__)



@app.route('/')
def home():
    states = 







if __name__ == '__main__':
    app.run(debug=False)