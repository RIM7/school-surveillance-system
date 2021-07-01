# import cv2

# # 1.creating a video object
# video = cv2.VideoCapture(0, cv2.CAP_DSHOW) 
# # 2. Variable
# a = 0
# # 3. While loop
# while True:
#     a = a + 1
#     # 4.Create a frame object
#     check, frame = video.read()
#     # Converting to grayscale
#     #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     # 5.show the frame!
#     cv2.imshow("Capturing",frame)
#     # 6.for playing 
#     key = cv2.waitKey(1)
#     if key == ord('q'):
#         break
# # 7. image saving
# showPic = cv2.imwrite("filename.jpg",frame)
# print('show: ', showPic)
# # 8. shutdown the camera
# video.release()
# cv2.destroyAllWindows()







# import cv2
# import numpy as np
# import os
# import mysql.connector as connector

# # ===================================================================
# # ===================================================================

# def register_parent():

# 	# ===================================================================
# 	# Take inputs. ======================================================
# 	# Name of the parent ================================================
# 	parent_name = input('Enter your name: ')

# 	# Read the parent_dir_count file. ===================================
# 	parent_dir_count = open("directory_counts/parent_dir_count.txt","r")
# 	parent_dir_no = parent_dir_count.readline()
# 	# Close the file
# 	parent_dir_count.close()

# 	# Open the same file in write mode.
# 	parent_dir_count = open("./directory_counts/parent_dir_count.txt","w")
# 	# Increment the count.
# 	parent_dir_count.write( str(int(parent_dir_no) + 1) )
# 	# Close the file
# 	parent_dir_count.close()
# 	print('count = ', parent_dir_no)

# 	# Phone no. of the parent. ==========================================
# 	phone_no = input('Enter your phone no.: ')


# 	# ===================================================================
# 	# Register parent to database =======================================
# 	connection = connector.connect(host="localhost",port=3306, user="root", passwd="root", database="surv_sys")
# 	# Set up the cursor
# 	cursor = connection.cursor()
# 	query = "insert into surv_sys(parent_name, dir_no, phone_no) values('{}', '{}', '{}');".format(parent_name, str(int(parent_dir_no) + 1), phone_no)

# 	cursor.execute(query)
# 	connection.commit()


# 	# ===================================================================
# 	# Take 12 photos of that parent using a photoburst. =================
# 	# Store them in 's'+ str(parent_dir_no)

# 	# Create directory
# 	print('parent_dir_no: ', str(int(parent_dir_no) + 1) )
# 	directory = 's' + str(int(parent_dir_no) + 1)
# 	parent_dir = "../training-data/Parent/"
# 	path = os.path.join(parent_dir, directory)
# 	os.mkdir(path)


# 	cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) 	#captureDevice = camera
# 	cv2.namedWindow("Capture image")
# 	img_counter = 0
# 	while True:
# 		ret, frame = cam.read()
# 		if not ret:
# 			print("failed to grab frame")
# 			break

# 		cv2.imshow("test", frame)
# 		k = cv2.waitKey(1)

# 		if k%256 == 27 or img_counter > 12:			# ESC pressed
# 			print("Closing...")
# 			break

# 		elif k%256 == 32: 							# SPACE pressed
# 			img_name = path + '/opencv_frame_{}.png'.format(img_counter)
# 			cv2.imwrite(img_name, frame)
# 			print("{} written!".format(img_name))
# 			img_counter += 1
# 	cam.release()
# 	cv2.destroyAllWindows()











# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# import cv2
# import numpy as np
# import mysql.connector as connector

# from data_preparation import DataPreparation
# from model import FaceRecogniser
# from prediction import Prediction

# from util import register_person



# def seek_entry(identity):
# 	# Data will be in two lists of same size: 
# 	# 	1. all the faces
# 	#	2. labels for each face
# 	print("Preparing data...")

# 	# print( prepare_training_data("D:/Project/training-data") )
# 	# *******************************************************************************
# 	# Train the model based on student folder or parent folder. Take that as a parameter.
# 	faces, labels = DataPreparation().data_preparation("../training-data")
# 	print("Data prepared")

# 	#print total faces and labels
# 	print("Total faces: ", len(faces))
# 	print("Total labels: ", len(labels))

# 	face_recognizer = FaceRecogniser().create_model()

# 	# Train
# 	face_recognizer.train(faces, np.array(labels))

# 	# Prediction
# 	# Read from a file all the person's name and store it in subjects list.
# 	subjects = ["", "Richik_Majumder", "Somhita_Majumder"]

# 	# Load test images
# 	test_img1 = cv2.imread('../test-data/s1/opencv_frame_0.png')
# 	# test_img1 = cv2.imread('../test-data/s1/opencv_frame_3.png')
# 	# test_img1 = cv2.imread('C:/Users/RiM/Downloads/Wallpapers/red_mountains.jpg')
# 	test_img1 = cv2.imread('C:/Users/RiM/OneDrive/Pictures/Camera Roll/false_test.jpg')

# 	# Perform a prediction
# 	predicted_img = Prediction().predict(test_img1, subjects, face_recognizer)

# 	if predicted_img == None:
# 		print('Face did not match.')
# 		return
# 	if predicted_img.all() == None:
# 		print("No face detected. Can't recognize parent or child.")
# 	else:
# 		print("Prediction complete")

# 		print('Showing Images')
# 		cv2.imshow(subjects[1], predicted_img)
# 		cv2.waitKey(0)
# 		cv2.destroyAllWindows()

# 		print(':( ?')


# if __name__=='__main__':

# 	seek_entry('parent')

# 	# while True:
# 	# 	choice = input('Enter your choice:\n\t1. Register yourself.\n\t2. Seek entry.\n\t3. Exit.\n')
# 	# 	if choice == '3':
# 	# 		print('Program ends.')
# 	# 		break

# 	# 	elif choice == '1':
# 	# 		parent_or_student = input('Choose your identity:\n\t1. Register as a parent.\n\t2. Register as a student.\n\t3. Exit.\n')

# 	# 		if parent_or_student == '1':
# 	# 			register_person('parent')
# 	# 		elif parent_or_student == '2':
# 	# 			register_person('student')
# 	# 		else:
# 	# 			break

# 	# 	elif choice == '2':
# 	# 		parent_or_student = input('Choose your identity:\n\t1. I am a as a parent.\n\t2. Register as a student.\n\t3. Exit.\n')

# 	# 		if parent_or_student == '1':
# 	# 			register_person('parent')
# 	# 		elif parent_or_student == '2':
# 	# 			register_person('student')
# 	# 		else:
# 	# 			break