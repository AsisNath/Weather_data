"""
Driving Assistance system will provide a message to the driver weather information
about the start and end location. The map will provide the distance and minimum time 
to reach the destination. The sensor data will detect a crash and call 911 or 
text to the family .  
Auther: Asis Nath 
"""
print(" The Auther :")
print("     /|    _____       ____ ")
print("    / |   |        |  |     ")
print("   /__|   |_____   |  |____ ")
print("  /   |        |   |      | ")
print(" /    |   _____|   |  ____| \n")
import requests 
endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = 'AIzaSyCLNO5mol_LjqDuOkTKLBke4Q9de-6GVy4'
#Asks the user to input Where they are and where they want to go.
origin = input('Where are you?: ').replace(' ','+')
destination = input('Where do you want to go?: ').replace(' ','+')
#Building the URL for the request
nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,api_key)
url = endpoint + nav_request
json_formate = requests.get(url).json()
#print(json_formate)
json_formate_ind = json_formate['routes'][0]['bounds']
#print(json_formate_ind)
json_formate_legs = json_formate['routes'][0]['legs']
#print(json_formate_legs)
json_formate_dist= json_formate_legs[0]['distance']['text']
print("Traveling distance")
print(json_formate_dist)
json_formate_start_zip= json_formate_legs[0]['start_address']
print("Starting address")
print(json_formate_start_zip)
json_formate_end_zip= json_formate_legs[0]['end_address']
print("Destination address")
print(json_formate_end_zip)
#start_zip = json_formate_start_zip[33:38]
start_zip = json_formate_start_zip[-10:-5]
#print(start_zip)
end_zip = json_formate_end_zip[-10:-5]
#print(end_zip)
api_address_openweather = 'http://api.openweathermap.org/data/2.5/weather?zip='
#user_zip =input ('Enter your zipcode: ')
user_zip_start =start_zip
user_zip_end =end_zip
usa_city = (',us')
api_key = '&appid=a371e67e3caa0ab622264a1323fa983f'
#url = api_address_openweather+user_zip+usa_city+api_key
url_start = api_address_openweather+user_zip_start+usa_city+api_key
url_end = api_address_openweather+user_zip_end+usa_city+api_key
#json_formate = requests.get(url).json()
json_formate_start = requests.get(url_start).json()
json_formate_end = requests.get(url_end).json()
#print(json_formate_end)
#print(json_formate)
#print(json_formate_start)
print('weather: ')
#json_formate_St = json_formate_start['weather'][0]['main']
#json_formate_en = json_formate_end['weather'][0]['main']
#print(json_formate_ind)
print('temp at starting location:')
print (json_formate_start['main']['temp'])
print('temp at Destinaiton:')
print (json_formate_end['main']['temp'])
print('wind speed at starting location ')
print (json_formate_start['wind']['speed'])
print('wind speed at Destinaiton')
print (json_formate_end['wind']['speed'])
print('clouds at starting location')
print (json_formate_start['clouds']['all'])
print('clouds at Destination')
print (json_formate_end['clouds']['all'])

