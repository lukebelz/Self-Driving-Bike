import threading
import numpy as np

from lidar import Lidar
from gps import GPS
from cameras import Cameras
# py vesc import tty.usbserial

# load lidar
#lidar = Lidar('/dev/tty.SLAB_USBtoUART')

#load GPS
#gps = GPS('/dev/tty.usbserial-1A1330', 4800, 5)

cameras = Cameras(1, 2, 0)
cameras.start()

#t1 = threading.Thread(target=lidar.start) 
#t2 = threading.Thread(target=gps.start)
  
# starting thread 1 
#t1.start() 
# starting thread 2 
#t2.start() 
  
# wait until thread 1 is completely executed 
#t1.join() 
# wait until thread 2 is completely executed 
#t2.join()