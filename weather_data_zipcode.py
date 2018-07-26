# -*- coding: utf-8 -*-
"""
Weather data by zipcode 
Asis Nath 
"""
print("     /|    _____       ____ ")
print("    / |   |        |  |     ")
print("   /__|   |_____   |  |____ ")
print("  /   |        |   |      | ")
print(" /    |   _____|   |  ____| \n")

import requests 
#api_address_openweather = 'http://api.openweathermap.org/data/2.5/weather?=a371e67e3caa0ab622264a1323fa983f&zip='
api_address_openweather = 'http://api.openweathermap.org/data/2.5/weather?zip='
user_zip =input ('Enter your zipcode: ')
usa_city = (',us')
api_key = '&appid=a371e67e3caa0ab622264a1323fa983f'
url = api_address_openweather+user_zip+usa_city+api_key
json_formate = requests.get(url).json()
print('weather')
json_formate_ind = json_formate['weather'][0]['main']
print(json_formate_ind)
print('temp')
print (json_formate['main']['temp'])
print('wind speed')
print (json_formate['wind']['speed'])
print('clouds')
print (json_formate['clouds']['all'])
print(json_formate)
