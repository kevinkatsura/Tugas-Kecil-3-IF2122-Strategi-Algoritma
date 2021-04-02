import requests
import smtplib

import webbrowser
import json
import tkinter


# API key
org = input("Masukkan asal: ")
dest = input("Masukkan tujuan: ")

# My API KEY
api_key = "AIzaSyCX_hR_mQiV3U-YyRr1MEfHPzXdBI0vG7U"
# URL
url = "https://maps.googleapis.com/maps/api/directions/json?"

# GET RESPONSE
r = requests.get(url + "origin=" + org + "&destination=" + dest + "&key=" +api_key)
distance = r.json()["routes"][0]["legs"][0]["distance"]["text"]
# label4 = tkinter.Label(main.window,text = directions)
# label4.grid(row = 3 , column = 0)


