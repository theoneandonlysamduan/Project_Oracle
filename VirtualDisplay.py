import pygame

pygame.init()

#x and y are dimensions of the window. 
x = 500
y = 309

#Opens the time and weather files for process
date_time_file    = open('Time'   , 'r')
city_weather_file = open('Weather', 'r')
#Puts the file content into the variables as lists of strings
date_time    = date_time_file.readlines()
city_weather = city_weather_file.readlines()
#Fetches the information from the lists of strings
date        = date_time[0]
time        = date_time[1]
city        = city_weather[0]
weather     = city_weather[1]
temperature = city_weather[2]

#Sets the window. Working. 
def set_window():
	window_caption = 'Project Oracle'
	screen = pygame.display.set_mode((x,y))		#Sets the size
	pygame.display.set_caption(window_caption)	#Sets the title
	#Sets the background
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((150, 150, 150))
	
	screen.blit(background, (0, 0))				#Applies the background
	pygame.display.flip()						#Refreshes the window

#Adds the time. 
def display_time():
	

