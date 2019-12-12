from flask import Flask, request, jsonify
from service import sightingsService
from service import flowerService

app = Flask(__name__)


@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
    return response

@app.route("/")
def hello():
    return jsonify(flowerService().getNames())

@app.route("/top/<name>", methods=["GET"])
def list_top10(name):
    return jsonify(sightingsService().topTen(name))

@app.route("/input", methods=["POST"])
def insert_sighting():
    sightingsService().create(request.form)
    return "added to Database"


if __name__ == "__main__":        # on running python app.py
    app.run()                     # run the flask app