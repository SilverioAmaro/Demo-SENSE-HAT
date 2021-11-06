from sense_hat import SenseHat 
sense = SenseHat() 
while True:
 orientation = sense.get_orientation()
 pitch = orientation['pitch']
 roll = orientation['roll']
 yaw = orientation ['yaw']
 print("pitch={0}, roll={l}, yaw={2}".format(pitch,yaw,roll))
