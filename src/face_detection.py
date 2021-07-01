import cv2
import numpy as np
#import matplotlib.pyplot as plt




# Face Detection
class FaceDetection:

	# Function to detect face using OpenCV
	def detect_face(self, img):
		# Convert the test image to gray scale as opencv face detector expects gray images
		self.gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		
		#===================================================================
		# Load OpenCV face detector:
		
		# LBP
		# face_cascade = cv2.CascadeClassifier('D:/Project/lbpcascade/lbpcascade_frontalface.xml')

		# Haar classifier
		self.face_cascade = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_default.xml')
		

		# Detect multiscale images(some images may be closer to camera than others) 
		# Result : [] of faces ( type: np.ndarray: checked while debugging )
		self.faces = self.face_cascade.detectMultiScale(self.gray, scaleFactor=1.2, minNeighbors=5);
		
		# No faces detected: Return None
		if (len(self.faces) == 0):
			return None, None, 0

		#===================================================================
		# Print the number of faces found
		# print('Faces found: ', len(self.faces))
		
		
		# Go over list of faces and draw them as rectangles on original colored
		for (x, y, w, h) in self.faces:
			cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
		
		# Convert image to RGB and show image
		# plt.imshow(convertToRGB(img))
		
		# Under the assumption that there will be only one face, extract the face area
		x, y, w, h = self.faces[0]

		# Return only the face part of the image
		return self.gray[y:y+w, x:x+h], self.faces[0], len(self.faces)


# FaceDetection().detect_face( cv2.imread('D:/Project/images/face2.jpg') )
