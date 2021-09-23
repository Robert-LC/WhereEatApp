from flask import Flask, render_template, request, url_for
from flask.helpers import url_for
from werkzeug.utils import redirect
import config # File wih API keys
import requests # Webcalls
import pandas as pd #Turn response into a dataframe



#Instantiates the Flask App
app = Flask(__name__)

# Show Index HTML, take user submission and pass it to results page
@app.route('/', methods = ['POST', 'GET']) # Decorator that flask uses to assign the url
def index():
    if request.method == 'POST':
        zipCode = request.form['zipCodeInput']
        return redirect(url_for('results'))
    else:
        return render_template('index.html')


@app.route('/results', methods = ['POST', 'GET'])
def getResults():
    data = getZipCodeResults(request.form['zipCodeInput'])
    return render_template('results.html', data = data)

# Function gets response from ZipCode Api, converts it to JSON, then turns JSON into a dictionary of info with user entered zipcode.
def getZipCodeResults(zip):
    r = requests.get(f'https://www.zipcodeapi.com/rest/{config.ZipKey}/info.json/{zip}/degrees')
    zipJson = r.json()

    # Pass the zip Codes info (City, State, Long, Lat into a dictionary)
    zipCodeDict = {
        'city' : zipJson['city'],
        'state' : zipJson['state'],
        'lattitude' : zipJson['lat'],
        'longitude' : zipJson['lng'],
    }
    return zipCodeDict
    
    
if __name__ == '__main__':
        app.run(debug=True)