from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route("/demo")
def demo():
	return render_template("demo.html")