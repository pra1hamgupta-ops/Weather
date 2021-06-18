from flask import Flask, render_template,request,redirect,url_for
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/weather',methods=[ 'GET','POST'])
def apiCall():
    city =""
    if request.method == 'POST':
        city = request.form['city']

    url = "https://community-open-weather-map.p.rapidapi.com/find"

    querystring = {"q":city,"cnt":"1","mode":"null","lon":"0","type":"link, accurate","lat":"0","units":"metric"}

    headers = {
        'x-rapidapi-key': "USE YOUR OWN RAPID API KEY HERE, Check Readme",
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    jsonObject = json.loads(response.text)

    return render_template('weather.html',json = jsonObject)
    

if __name__ == '__main__':
    app.run()

