import pygame
import RPi.GPIO as GPIO
from gpiozero import Button
from gpiozero import Motor
from time import sleep

btn1 = Button(20)
btn2 = Button(21)
motor = Motor(4, 14)

pygame.init()


try:
	while True:       
		while True:
			
			motor.stop()
			music = pygame.mixer.music.load('sounds/sound1.mp3')
			pygame.mixer.music.play()
			sleep(3)  #working time  
			motor.forward()
			sleep(3)  #pause
			
			if btn1.is_pressed:
				pygame.mixer.music.stop()
				print('pressed')
				motor.stop()
				music = pygame.mixer.music.load('sounds/sound2.mp3')
				pygame.mixer.music.play()
				sleep(3)  #working time   
				motor.forward()
				sleep(3)#pause
				
			if btn2.is_pressed:
				pygame.mixer.music.stop()
				print('pressed')
				motor.stop()
				music = pygame.mixer.music.load('sounds/sound3.mp3')
				pygame.mixer.music.play()
				sleep(3)  #working time     
				motor.forward()
				sleep(3)#pause
        
            
finally: GPIO.cleanup()        
