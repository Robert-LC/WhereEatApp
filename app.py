from flask import Flask, render_template, request
import config # File wih API keys
import requests # Webcalls
import pandas as pd #Turn response into a dataframe



#Instantiates the Flask App
app = Flask(__name__)

@app.route('/', methods=['POST']) # Decorator that flask uses to assign the url
def getIndex():
    return render_template('index.html')

@app.route('/results')
def getResults():
    data = searchZipCode(37604) 
    return render_template('results.html', data=data)

# Function gets response from ZipCode Api, converts it to JSON, then turns JSON into a dictionary of info with user entered zipcode.
def searchZipCode(zip):
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
    
    
def getUserSubmit():
    zipCode = request.form.get('zipCode')
    return zipCode

if __name__ == '__main__':
        app.run(debug=True)