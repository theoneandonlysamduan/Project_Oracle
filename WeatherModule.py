import urllib.request
import json
from os import remove

response = urllib.request.urlopen('http://api.wunderground.com/api/386a8e8ab04d7748/conditions/q/NH/Manchester.json')
res = json.load(response)

obs_rst = res['current_observation']			#Fetches the observation results as a large dictionary

loc_info= obs_rst['display_location']			#Fetches the location subdictionary
def location(): 
	city 	= loc_info['city']					#Fetches city name
	state 	= loc_info['state']					#Fetches state name
	
	endString = city + ' ' + state				#Processes two strings into one for final output
	return endString
#location() works and returns a string that looks like "San Fran CA". 

weather	= obs_rst['weather']					#Fetches weather as a string
temp 	= str(obs_rst['temp_c']) + ' degrees Celsius'			#Fetches temperature, outputs something like "20℃"
loc		= location()							#Fetches location

final_str = loc + '\n' + weather + '\n' + temp
#Makes the final string, outputs something like "Manchester NH, Mostly Cloudy, 4.7℃". 
remove('Weather')
f = open('Weather', 'w+')
f.write(final_str)
