from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp


app = Flask(__name__)

counter = 0

@app.route("/", methods=["GET", "POST"])
def tester():
    counter+=1
    return render_template("index.html")