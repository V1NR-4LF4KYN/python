# Stopwatch Program in Python3
# 
# Stopwatch is controllable by pressing the 'space-bar' to pause 
# and also resume the stopwatch respectively.
#
# 
# Author: p4zzz
# 06.06.2021




import time
from pynput.keyboard import Key, Listener 


class Stopwatch:
	def __init__(self):
		self.time: float = 0					# Total Time, includes all seconds since start so you can pause
		self.START_TIME: float = 0				# Time at start of program
		self.current_time: float = 0 			# Current Time while stopping it	
		self.running: bool = False				# Bool to control pause of watch
		self.flipped: bool = False				# switches to True when unpaused

		self.listener = Listener(self.on_press) # listener for keyboard input
		self.listener.start()					# starts listener


	def on_press(self, key):					# func controls pause/resume of watch
		if key==Key.space:						# key is space-bar-key
			if self.running:
				self.running = False
			else:
				self.running = True

	def stopTime(self):						# if not paused print time
		while True:							# ctrl+c 'able due to try-except-block because of endless loop
			try:
				if self.running:			# if unpaused 
					if not self.flipped:	# first set start time one more time. Then stop. Only does it when flipped is False
						self.START_TIME = time.time()	
						self.flipped = True	
					self.current_time = (time.time() - self.START_TIME) # current time is time right then minus the start time
					print(f'{self.current_time + self.time:.3f}') # printing current time + all other times we measured beefore AND rounding it to 3 decimal points
					time.sleep(0.001) # after each step sleep 0.001 secs
				else: 
					self.flipped = False					# reset flip when paused
					self.time += self.current_time			# add current time to total time
					self.current_time = 0 					# current time = 0, so loop doesnt add more
			except:	
				print('Something went wrong. Exiting...')
				break


t = Stopwatch()
t.stopTime()