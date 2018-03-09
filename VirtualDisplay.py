import pygame, os
from pygame.locals import *
from time import sleep

pygame.init()
font = pygame.font.SysFont('roboto', 40)
#x and y are dimensions of the window. 
x = 500
y = 309
screen = pygame.display.set_mode((x,y))	#Sets the size

#Sets the window. Working. 
def set_window():
	window_caption = 'Duanaweather'
	pygame.display.set_caption(window_caption)	#Sets the title
	#Sets the background
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((150, 150, 150))
	
	screen.blit(background, (0, 0))				#Applies the background
	pygame.display.flip()						#Refreshes the window

#Adds the time. 
def display_time():

	try: 
		date_time_file = open('Time'   , 'r')
	except FileNotFoundError: 
		return
	
	date_time      = date_time_file.readlines()
	#If clause: If time file is empty(created by 'open'), skip this function. 
	if os.stat('Time').st_size == 0:
		return
		
	date = date_time[0]
	time = date_time[1]
	date = date[:10]			#Gets rid of the \n at the end of the line
	
	time_label = font.render(time, 1, (255, 255, 255))
	date_label = font.render(date, 1, (255, 255, 255))
	
	screen.blit(time_label, (5  , 5))
	screen.blit(date_label, (230, 5))
	
	pygame.display.flip()

def display_weather():
	try: 
		city_weather_file = open('Weather', 'r')
	except FileNotFoundError: 
		return
		
	city_weather      = city_weather_file.readlines()
	#If clause: If weather file is empty, skip this function. 
	if os.stat('Weather').st_size == 0:
		return
		
	city        = city_weather[0]
	city		= city   [:len(city)-1]
	weather     = city_weather[1]
	weather 	= weather[:len(weather)-1]
	temperature = city_weather[2]
	
	weather_label     = font.render(weather    , 1, (255, 255, 255))
	loc_label         = font.render(city       , 1, (255, 255, 255))
	temperature_label = font.render(temperature, 1, (255, 255, 255))
	
	screen.blit(weather_label    , (5  , 35))
	screen.blit(loc_label        , (5  , 60))
	screen.blit(temperature_label, (230, 35))
	
	pygame.display.flip()

def reset_window():
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((150, 150, 150))
	
	screen.blit(background, (0, 0))				#Applies the background
	pygame.display.flip()						#Refreshes the window

set_window()
while True: 
	sleep(0.5)
	reset_window()
	display_time()
	display_weather()
	for event in pygame.event.get():
		if (event.type == QUIT):		#Currently not quitting
			break
	
