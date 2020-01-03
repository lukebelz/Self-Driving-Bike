import numpy as np
import cv2

class Cameras:
	def __init__(self, leftId, centerId, rightId):

		print("Opening Cameras...")

		self.left = cv2.VideoCapture(leftId)
		self.center = cv2.VideoCapture(centerId)
		self.right = cv2.VideoCapture(rightId)

		self.imageLeft = None
		self.imageCenter = None
		self.imageRight = None
		self.imageComplete = None

	def start(self):
		while(True):
			retL, self.imageLeft = self.left.read()
			retC, self.imageCenter = self.center.read()
			retR, self.imageRight = self.right.read()

			self.imageComplete = np.concatenate((self.imageLeft, self.imageCenter), axis=1)
			self.imageComplete = np.concatenate((self.imageComplete, self.imageRight), axis=1)

			cv2.imshow('Bike',self.imageComplete)

			if cv2.waitKey(1) & 0xFF == ord('q'):
				self.stop()

	def stop(self):
		cap.release()
		cv2.destroyAllWindows()