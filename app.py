from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template ("index.html")

@app.route("/weatherapp" , methods = ['POST' , "GET"])
def get_weatherdata():
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'q' : request.form.get('city'),
         'appid' : request.form.get('appid'),
         'units' : request.form.get('units')}
    response = requests.get(url,params=params)
    data = response.json()
    city = data['name']
    data_main = data['main']
    max_temp = data_main['temp_max']  
    return f"For City of : {city} hightest temp is {max_temp}"



if __name__ == '__main__':
    app.run(host="0.0.0.0")
