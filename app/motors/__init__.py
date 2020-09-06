import RPi.GPIO as GPIO

class Motor():

	def __init__(self, driver="DRV8825", model="NEMA17", number=0):

		self.driver = driver
		self.model = model
		self.number = number

		if driver == "DRV8825":

			if number == 1:

				self.dir_pin = 13
				self.step_pin = 19        
				self.enable_pin = 12
				self.mode_pins = (16, 17, 20)

			elif number == 2:

				self.dir_pin = 24
				self.step_pin = 18        
				self.enable_pin = 4
				self.mode_pins = (21, 22, 27)

		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(self.dir_pin, GPIO.OUT)
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

	def start(self):

		self.set_pin(self.enable_pin, 0)

	def stop(self):

		self.set_pin(self.enable_pin, 1)
