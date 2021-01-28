from flask import Flask, render_template, request, jsonify
from markupsafe import escape
import json
import utils

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/api/search/')
def search():
    entity_type = request.args.get('key')
    entity_id = request.args.get('id')
    return jsonify(utils.requestedData(entity_type,entity_id))

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html"), 404

if __name__ == '__main__':
    app.run(debug=True)
