# Stopwatch Program in Python3
# 
# Stopwatch is controllable by pressing the 'space-bar' to pause 
# and also resume the stopwatch respectively.
#
# 
# Author: p4zzz
# 06.06.2021


# TODO: figure out way to stop time measuring when paused. 


import time
from pynput.keyboard import Key, Listener 


class Stopwatch:
	def __init__(self):
		self.START_TIME = time.time()			# Time at start of program
		self.running: bool = True				# Bool to control pause of watch

		self.listener = Listener(self.on_press) # listener for keyboard input
		self.listener.start()					# starts listener


	def on_press(self, key):					# func controls pause/resume of watch
		if key==Key.space:						# key is space-bar-key
			if self.running:
				self.running = False
			else:
				self.running = True

	def stopTime(self):							# if not paused print time
		while True:								# ctrl+c 'able due to try-except-block because of endless loop
			try:
				if self.running:			
					print(f'{time.time() - self.START_TIME:.3f}') # rounding it to 3 decimal points
					time.sleep(0.001)
			except:	
				print('Something went wrong. Exiting...')
				break


t = Stopwatch()
t.stopTime()