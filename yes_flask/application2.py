from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	headline="hello VIVIEN"
	return render_template("monblog.html" , headline=headline)