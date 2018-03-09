from subprocess import call
import time, sys, termios, tty, os
 


set_time_interval    = 1				#Interval between every update of time
set_weather_interval = 200				#Interval between every update of weather
#The WeatherModule will be called once in 20 mins, the TimeModule will be called every second. The DisplayModule will be called every time when there is an update. 
#The DisplayModule is still work in progress. 

print('Please visit https://www.wunderground.com/?apiref=c68c74f9a26733fa to provide me with free API access. Thanks!')

def WeatherModule():
	call(['python3 WeatherModule.py'], shell = True)

def TimeModule():
	call(['python3 TimeModule.py'], shell = True)

#This piece of code is used to detect the keystroke so that there is a way of quitting the program. Not working yet. 
#def getch():
#    fd = sys.stdin.fileno()
#    old_settings = termios.tcgetattr(fd)
#    try:
#        tty.setraw(sys.stdin.fileno())
#        ch = sys.stdin.read(1)
# 
#    finally:
#        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
#    return ch

interval_time 	 = 0
interval_weather = 0
#Those two variables are used to caculate separately the time interval for weather update and time update
timeCache    = time.clock_gettime(time.CLOCK_REALTIME)//1	
weatherCache = time.clock_gettime(time.CLOCK_REALTIME)//1

#print('Press "q" to quit')
while True:
	current_time = time.clock_gettime(time.CLOCK_REALTIME)//1
	#interval_time records the current time from the last trigger of TimeModule. 
	#interval_weather records the current time from the last trigger of WeatherModule. 
	interval_time    = current_time-timeCache
	interval_weather = current_time-weatherCache
	#key = getch()
	
	#This if clause is triggered once every second to update the time, resets the time counter and updates the time
	if (interval_time >= set_time_interval):
		#print('Time Updated')				#Print is for debugging
		TimeModule()
		interval_time = 0
		timeCache = current_time
		
	#This if clause is triggered once every 200 secs to update the weather, then resets the weather counter. 
	if (interval_weather >= set_weather_interval): 
		#print('Weather Updated')			#Print is for debugging
		WeatherModule()
		interval_weather = 0
		weatherCache = current_time
	
	#if (key == 'q'):
	#	print('Terminated.')
	#	break
	#if (key == ''): 
	#	pass
