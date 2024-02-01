from flask import Flask, render_template
import requests
import os
import time
from datetime import date


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/nasa')
def nasa():
    
    today = str(date.today())    
    response = requests.get("https://api.nasa.gov/planetary/apod?api_key=GdHGB6sVubfXxXmS8Gsp5N8f9INB4hDuQqdTafOl&date="+today)
 
    data= response.json()
    
    print(data['explanation'])
    
    return render_template('nasa.html' , data=data)
    
@app.route('/dynamic')
def dynamic():
    
    greeting="Team Edge is in the house!"
    friends = ["Cardi", "Janelle", "Kali", "Jorja", "Rosalia", "Karol"]
    return render_template('dynamic.html', greeting=greeting, friends=friends)
    
    
@app.route('/info')
def info():
    
    temp = os.popen("vcgencmd measure_temp").readline()
    ipaddr = os.popen(" hostname -I").readline()
    freemem = os.popen("df | grep 'Used' | uniq ").readline()
    cpuinfo = os.popen("cat /proc/cpuinfo  | grep 'model name\|Hardware\|Serial' | uniq").readline()
    uptime = os.popen("uptime -p").readline()
    
    return render_template('info.html', temp=temp, ipaddr=ipaddr, freemem=freemem, cpuinfo=cpuinfo, uptime=uptime)

if __name__ == '__main__':
    app.run( debug=True, host='0.0.0.0', port=2022)
