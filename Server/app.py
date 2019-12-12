from flask import render_template
from flask import Flask, request, jsonify, render_template, redirect, url_for
from service import sightingsService
from service import flowerService

app = Flask(__name__)
names = flowerService().getNames()

@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
    return response

@app.route("/")
def hello():
    return render_template('home.html', names = names)

@app.route('/addSighting')
def addSighting():
    return render_template('adding.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route("/top/<name>", methods=["GET"])
def list_top10(name):
    return jsonify(sightingsService().topTen(name))

@app.route("/input", methods=["POST"])
def insert_sighting():
    print(request.form)
    sightingsService().create(request.form)
    return "added to Database"


if __name__ == "__main__":        # on running python app.py
    app.run()                     # run the flask app