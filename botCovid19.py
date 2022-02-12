import requests
from win10toast import ToastNotifier
import json 
import time

def update():
    r = requests.get('http://coronavirus-19-api.herokuapp.com/all')
    data = r.json()
    text = f'Cases: {data["cases"]} \nDeaths: {data["deaths"]} \nRecovered: {data["recovered"]}'

    while True:
        toast = ToastNotifier()
        toast.show_toast("Covid 19 Update", text, duration=10)
        time.sleep(11)

update()

