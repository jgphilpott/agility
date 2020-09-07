import time

from threading import Thread
from multiprocessing import Process

from motors import Motor

M0 = Motor("DRV8825", "NEMA-17", 1)
M1 = Motor("DRV8825", "NEMA-17", 2)
M2 = Motor("DRV8825", "28BJY-48", 1)
M3 = Motor("DRV8825", "28BJY-48", 2)

motors = {"M0": M0, "M1": M1, "M2": M2, "M3": M3}

def start(motor, mode="1"):

	motors[motor].start(str(mode))

def stop(motor):

	motors[motor].stop()

def turn(motor, direction="forward", degrees=360, duration=1, mode="1", auto_stop=False):

	motors[motor].turn(direction, degrees, duration, str(mode), auto_stop)

def step(motor, direction="forward", degrees=360, duration=1, mode="1", auto_stop=False, thread=True):

	if thread:

		Thread(target=turn, args=(motor, direction, degrees, duration, str(mode), auto_stop)).start()

	else:

		turn(motor, direction, degrees, duration, str(mode), auto_stop)
