# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
from model import getImageUrlFrom
import os
import requests 
# -- Initialization section --
app = Flask(__name__)
# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time = datetime.now())
# add route for giph results
@app.route("/yourgif",methods = ['GET', 'POST'] )
def yourgif():
    # gets the giph for giphy and puts the link on webpage
    user_response = 'dog'
    gif_url = getImageUrlFrom(user_response)
    
    # pass url to render template and have that url appear as an image in yourgif.html
    return render_template("yourgif.html",time = datetime.now(), gif_url = gif_url)

    # datetime.now gets the updated time and code for css. Tricks browser in updating to think its real time.