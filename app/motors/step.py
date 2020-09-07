import time

from threading import Thread
from multiprocessing import Process

from motors import Motor

M0 = Motor("DRV8825", "NEMA-17", 1)
M1 = Motor("DRV8825", "NEMA-17", 2)
M2 = Motor("DRV8825", "28BJY-48", 1)
M3 = Motor("DRV8825", "28BJY-48", 2)

motors = [M0, M1, M2, M3]
