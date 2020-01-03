from lidar import Lidar
from gps import GPS
# py vesc import tty.usbserial

# load lidar
lidar = Lidar('/dev/tty.SLAB_USBtoUART')

#load GPS
gps = GPS('/dev/tty.usbserial-1A1330', 4800, 5)
