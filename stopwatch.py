# Stopwatch Program in Python3
# 
# Stopwatch is controllable by pressing the 'space-bar' to pause 
# and also resume the stopwatch respectively.
#
# 
# Author: p4zzz
# 06.06.2021

# TODO: fix key detection issue, which prevents quitting program by pressing q
# TODO 2: add lap functionality


import time
from pynput.keyboard import Key, Listener 


class Stopwatch:
	def __init__(self):
		self.time: float = 0					# Total Time, includes all seconds since start so you can pause
		self.START_TIME: float = 0				# Time at start of program
		self.current_time: float = 0 			# Current Time while stopping it	
		self.unpaused: bool = False				# Bool to control pause of watch
		self.flipped: bool = False				# switches to True when unpaused
		self.running: bool = True				# Bool to control wether program is running

		self.listener = Listener(self.on_press) # listener for keyboard input
		self.listener.start()					# starts listener

												# Inform user over possibilities
		print('Press \'space\' to Start...')
		print('Press \'space\' again to pause...')
		print('Press \'l\' to lap...') # TODO
		print('Press \'q\' to quit...')


	def on_press(self, key):					# func controls pause/resume of watch
		print(key)
		if key==Key.space:						# key is space-bar-key
			if self.unpaused:
				self.unpaused = False
			else:
				self.unpaused = True
		elif key=='q':							# if q is pressed quit the program
			self.running = False

	def stopTime(self):						
		while self.running:								# if not paused print time
			try:										# ctrl+c 'able due to try-except-block because of endless loop
				if self.unpaused:						
					if not self.flipped:				# first set start time one more time. Then stop. Only does it when flipped is False
						self.START_TIME = time.time()	
						self.flipped = True	
					self.current_time = (time.time() - self.START_TIME) # current time is time right then minus the start time
					print(f'{self.current_time + self.time:.3f}') # printing current time + all other times we measured beefore AND rounding it to 3 decimal points
					time.sleep(0.001) # after each step sleep 0.001 secs
				else: 
					if self.flipped:
						print('Press \'space\' to resume...')
					self.flipped = False					# reset flip when paused
					self.time += self.current_time			# add current time to total time
					self.current_time = 0 					# current time = 0, so loop doesnt add more

			except:	
				print('Something went wrong. Exiting...')
				break


t = Stopwatch()
t.stopTime()