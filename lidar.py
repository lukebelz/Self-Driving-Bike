from rplidar import RPLidar

class Lidar:
	def __init__(self, port):
		self.port = port

		self.lidar = RPLidar('/dev/tty.SLAB_USBtoUART')

		info = self.lidar.get_info()
		print(info)

		health = self.lidar.get_health()
		print(health)

	def start(self):
		for i, scan in enumerate(self.lidar.iter_scans()):
			print('%d: Got %d measurments' % (i, len(scan)))
			if i > 100:
				break

		self.stop()

	def stop(self):
		self.lidar.stop()
		#self.lidar.stop_motor()
		#self.lidar.disconnect()