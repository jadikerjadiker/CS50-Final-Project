import os
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/')
def homepage():
    counter = 0 
    return render_template("tictactoe.html",counter=counter)

@app.route('/tictactoe')
def tictactoe():
    return render_template("tictactoe.html")
    





# even though this part does grab all the files now, it doesn't seem to be working
extra_dirs = ['../FrontEnd',]
extra_files = extra_dirs[:]
for extra_dir in extra_dirs:
    for dirname, dirs, files in os.walk(extra_dir):
        for filename in files:
            filename = os.path.join(dirname, filename)
            if os.path.isfile(filename):
                extra_files.append(filename)
print(len(extra_files))
print(extra_files)
app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), extra_files=extra_files)



















