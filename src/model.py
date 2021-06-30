import cv2


class FaceRecogniser:

	def create_model(self,):
		#==============================================================================
		#==============================================================================
		# Create our LBPH face recognizer 
		# The following line causes: 
		# Error: cv2.cv2 has no attribute 'face'.
		# No solution found for the current error.
		# Possible cause: cv2 has moved 'face' from their original repo to some support package repo.
		#face_recognizer = cv2.face.createLBPHFaceRecognizer()	


		# Model Creation.
		self.face_recognizer = cv2.face_LBPHFaceRecognizer.create()

		return self.face_recognizer





# FaceRecogniser()