from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	headline="bonjour monsieur comment allez vous?"
	return render_template("index.html" , headline=headline)

@app.route("/<string:name>")
def hello(name):
	name=name.capitalize()
	return f"Hello, {name}"