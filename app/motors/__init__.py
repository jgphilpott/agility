import time
import RPi.GPIO as GPIO

class Motor():

	def __init__(self, driver="DRV8825", model="NEMA-17", number=0):

		self.driver = driver
		self.model = model
		self.number = number

		if self.driver == "DRV8825":

			if self.number == 1:

				self.direction_pin = 13
				self.step_pin = 19
				self.enable_pin = 12
				self.mode_pins = (16, 17, 20)

			elif self.number == 2:

				self.direction_pin = 24
				self.step_pin = 18
				self.enable_pin = 4
				self.mode_pins = (21, 22, 27)

		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(self.direction_pin, GPIO.OUT)
		GPIO.setup(self.step_pin, GPIO.OUT)
		GPIO.setup(self.enable_pin, GPIO.OUT)
		GPIO.setup(self.mode_pins, GPIO.OUT)

	def set_pin(self, pin, value):

		GPIO.output(pin, value)

	def set_microstep(self, mode="1"):

		microstep = {"1": (0, 0, 0),
					"1/2": (1, 0, 0),
					"1/4": (0, 1, 0),
					"1/8": (1, 1, 0),
					"1/16": (0, 0, 1),
					"1/32": (1, 0, 1)}

		self.set_pin(self.mode_pins, microstep[mode])

	def start(self, mode="1"):

		self.set_microstep(mode)
		self.set_pin(self.enable_pin, 0)

	def stop(self):

		self.set_pin(self.enable_pin, 1)

	def turn(self, direction="forward", degrees=360, duration=1, mode="1", auto_stop=False):

		self.start(mode)

		if direction == "forward":

			self.set_pin(self.direction_pin, 0)

		elif direction == "backward":

			self.set_pin(self.direction_pin, 1)

		if self.model == "NEMA-17":

			self.steps = round((6400 / 360) * degrees)

		elif self.model == "28BJY-48":

			self.steps = round((65536 / 360) * degrees)

		self.step_delay = duration / self.steps

		for step in range(self.steps):

			self.set_pin(self.step_pin, True)
			time.sleep(self.step_delay)
			self.set_pin(self.step_pin, False)

		if auto_stop:

			self.stop()
