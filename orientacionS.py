#from sense_emu import SenseHat
from sense_hat import SenseHat
import time

sense = SenseHat()

roll, pitch, yaw = sense.orientation.values()
print("Pitch: %s, Roll: %s, Yaw: %s" % (pitch, roll, yaw))
