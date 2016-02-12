#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import numpy, pygame, os, random, sys
from pygame.locals import *
import pygame.sndarray
import pygame.mixer
import KeySoundDict


class MusicBox(object):

	def __init__(self, tuning):
		pygame.mixer.init()
		self.sample_rate = 44100
		self.key_dict = tuning
		
	def play_sound(self, array, volume_r, volume_l  ):
			
		beep = pygame.sndarray.make_sound(array)
		go = beep.play(-1)
		go.set_volume(volume_r, volume_l)
		
		def stop_sound():
			beep.stop()
				
		return stop_sound
	
	def sine_array_onecycle(self, hz, peak):
		length = self.sample_rate / float(hz)
		omega = numpy.pi * 2 / length
		xvalues = numpy.arange(int(length)) * omega
		return (peak * numpy.sin(xvalues))
    
    
	def sine_array(self, (hz, peak), n_samples = 44100):
		return numpy.resize(self.sine_array_onecycle(hz, peak), (n_samples,))
	
	def create_beat(self):
		pass
	
	def run(self):
		screen = pygame.display.set_mode((800,600))
		pygame.display.toggle_fullscreen()
		
		pygame.mixer.set_num_channels(8)
		
		pygame.init()
		count_index = 0
		sound_dict = dict()
		
		background = pygame.Surface(screen.get_size())
		backgroundspec = background.convert()
		backgroundspec = background.fill((0,255,255))
		screen.blit(background,backgroundspec)
		pygame.display.flip()
	
		while True:

			for event in pygame.event.get():
				#print event
				
				
				
				if event.type == KEYDOWN:
					
					keys = pygame.key.get_pressed()
					
					if keys[K_a] and keys[K_p]:
						print "Good Bye!!!!"
						sys.exit(0)

					
					test_tone = random.randint(30,3000)
					#print test_tone
					#tone = self.sine_array(keys.index(1)**2, 100) #Pulls out the 
					#print keys.index(1)
					tone =  self.sine_array(self.key_dict[keys.index(1)])
					
					tone = numpy.array(zip (tone , tone))
					stop = self.play_sound(tone , 0.2, 0.2) #
					count_index += 1
					sound_dict[count_index] = stop
				
				
				
				elif event.type == KEYUP:
					sound_dict[count_index]()
					
					count_index -= 1
				
				
						
				
				elif event.type == QUIT:
					sys.exit(0)
				
				backgroundspec = background.fill((random.randint(0,255),
												  random.randint(0,255),
												  random.randint(0,255))
												  )
												  
				screen.blit(background,backgroundspec)
				pygame.display.flip()
				
				#	print keys
			
if __name__ == '__main__':				
	MB = MusicBox(KeySoundDict.Key_Dict)
	MB.run()
					
##TODO ::: TUNE THIS THING			
##TODO ::: PERFORMANCE PERFORMANCE PERFORMACE
## PORT TO RASBERRY PI
