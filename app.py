from flask import Flask, render_template # Used to take the index.html to render it when flask is ran.
import requests
import json

#Instantiates the Flask App
app = Flask(__name__)

@app.route("/") # Decorator that flask uses to assign the url
def get_index():
    return render_template("index.html")