import cv2

from face_detection import FaceDetection



class Prediction:

	# Function to draw rectangle on image according to given (x, y) coordinates and given width and heigh
	def draw_rectangle(self, img, rect):
	    (x, y, w, h) = rect
	    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
	 
	#function to draw text on give image starting from passed (x, y) coordinates. 
	def draw_text(self, img, text, x, y):
	    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)



	#==============================================================================
	#==============================================================================
	# Prediction:
	# 		1. Recognize the person in image passed
	#		2. Draws a rectangle + name around detected face.

	def predict(self, test_img, subjects, face_recognizer):
		# Make a copy of the image as we don't want to change original image
		img = test_img.copy()

		#detect face from the image
		face, rect, no_of_faces = FaceDetection().detect_face(img)

		# We will not process images with multiple faces
		if no_of_faces > 1:
			return None

		else:
			#predict the image using our face recognizer 
			label = face_recognizer.predict(face)

			# Get name of respective label returned by face recognizer
			print('label= ', label[0])

			label_text = subjects[label[0]]
		 

			#draw a rectangle around face detected
			self.draw_rectangle(img, rect)

			#draw name of predicted person
			self.draw_text(img, label_text, rect[0], rect[1]-5)
			 
			# print(img)
			return img