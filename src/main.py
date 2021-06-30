import cv2
import numpy as np

from data_preparation import DataPreparation
from model import FaceRecogniser
from prediction import Prediction

if __name__=='__main__':
	
	# Data will be in two lists of same size: 
	# 	1. all the faces
	#	2. labels for each face
	print("Preparing data...")

	# print( prepare_training_data("D:/Project/training-data") )
	faces, labels = DataPreparation().data_preparation("../training-data")
	print("Data prepared")

	#print total faces and labels
	print("Total faces: ", len(faces))
	print("Total labels: ", len(labels))


	face_recognizer = FaceRecogniser().create_model()

	# Train
	face_recognizer.train(faces, np.array(labels))






	# Prediction
	# Read from a file all the person's name and store it in subjects list.
	subjects = ["", "Richik_Majumder", "Somhita_Majumder"]







	# Load test images
	test_img1 = cv2.imread('../test-data/s1/opencv_frame_0.png')

	#perform a prediction
	predicted_img = Prediction().predict(test_img1, subjects, face_recognizer)

	if predicted_img == None:
		print("Multiple faces detected. Can't recognize parent or child.")
	else:
		print("Prediction complete")

		print('Showing Images')
		cv2.imshow(subjects[1], predicted_img1)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

		print(':( ?')
