from flask import Flask, render_template, request, jsonify
from markupsafe import escape
import pandas as pd
import utils
import json
import convert

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/search/')
def search():
    entity_type = request.args.get('key','')
    return jsonify(convert.requestedData(entity_type))

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html"), 404

if __name__ == '__main__':
    app.run(debug=True)
