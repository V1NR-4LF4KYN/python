# Stopwatch Program in Python3
# 
# Stopwatch is controllable by pressing the 'space-bar' to pause 
# and also resume the stopwatch respectively.
#
# 
# Author: p4zzz
# 06.06.2021

# TODO: fix key detection issue, which prevents quitting program by pressing 'q'


from time import
from pynput.keyboard import Key, Listener , KeyCode


class Stopwatch:
	def __init__(self):
		self.time: float = 0					# Total Time, includes all seconds since start so you can pause
		self.START_TIME: float = 0				# Time at start of program
		self.current_time: float = 0 			# Current Time while stopping it	
		self.unpaused: bool = False				# Bool to control pause of watch
		self.flipped: bool = False				# switches to True when unpaused
		self.running: bool = True				# Bool to control wether program is running
		
		self.lap_times: list = []				# List for lap times
		self.time_counter: int = 0

		self.listener = Listener(self.on_press) # listener for keyboard input
		self.listener.start()					# starts listener

												# Inform user over possibilities
		print('Press \'space\' to Start...')
		print('Press \'space\' again to pause...')
		print('Press \'l\' to lap...') # TODO
		print('Press \'q\' to quit...')


	def on_press(self, key):					# func controls pause/resume of watch
		# print(f'Key: {key} pressed.')
		if key==Key.space:						# key is space-bar-key
			if self.unpaused:					# pause or unpause basically 
				self.unpaused = False
			else:
				self.unpaused = True			
				for lap in self.lap_times:						# after pausing display all lap times
					print(f'Lap {self.time_counter}: {lap}') 	# lap is the time

		if key==KeyCode(char='q'):								# if q is pressed quit the program
			self.running = False

		if key==KeyCode(char='l'):
			print(f'Time Added')
			self.time_counter += 1
			self.lap_times.append(self.current_time)	# append current time to lap-list



	def stopTime(self):
		while self.running:							# if not paused print time	
			if self.unpaused:						
				if not self.flipped:				# first set start time one more time. Then stop. Only does it when flipped is False
					self.START_TIME = time.time()	
					self.flipped = True				# flipped controls wether to print control to screen for user after pausing
				self.current_time = (time.time() - self.START_TIME) # current time is time right then minus the start time
				print(f'{self.current_time + self.time:.3f}') # printing current time + all other times we measured beefore AND rounding it to 3 decimal points
				time.sleep(0.001) 
			else: 
				if self.flipped:
					print('Press \'space\' to resume...')
					for time in self.lap_times:
						print(f'Lap: {time}\n')
				self.flipped = False					# reset flip when paused
				self.time += self.current_time			# add current time to total time
				self.current_time = 0 					# current time = 0, so loop doesnt add more



t = Stopwatch() 
t.stopTime()