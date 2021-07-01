import cv2
import numpy as np
import os
import mysql.connector as connector


from data_preparation import DataPreparation
from model import FaceRecogniser
from prediction import Prediction

# ===================================================================
# ===================================================================

def register_person(choice):

	# Establish connection to database.
	connection = connector.connect(host="localhost",port=3306, user="root", passwd="root", database="surv_sys")
	# Set up the cursor
	cursor = connection.cursor()


	# =======================================================================

	if choice == 'parent':
		# ===================================================================
		# Take inputs. ======================================================
		# Name of the parent ================================================
		parent_name = input("Enter parent's name: ")

		# Read the parent_dir_count file. ===================================
		parent_dir_count = open("directory_counts/parent_dir_count.txt","r")
		parent_dir_no = parent_dir_count.readline()
		# Close the file
		parent_dir_count.close()

		# Open the same file in write mode.
		parent_dir_count = open("./directory_counts/parent_dir_count.txt","w")
		# Increment the count.
		parent_dir_count.write( str(int(parent_dir_no) + 1) )
		# Close the file
		parent_dir_count.close()
		print('count = ', parent_dir_no)

		# Phone no. of the parent. ==========================================
		phone_no = input('Enter your phone no.: ')

		# ===================================================================
		# Register parent to database =======================================
		query = "insert into surv_sys(parent_name, dir_no, phone_no) values('{}', '{}', '{}');".format(parent_name, str(int(parent_dir_no) + 1), phone_no)
		cursor.execute(query)

		# ===================================================================
		# Take 12 photos of that parent using a photoburst. =================
		# Store them in 's'+ str(parent_dir_no)
		# Create directory

		try:
			print('parent_dir_no: ', str(int(parent_dir_no) + 1) )
			directory = 's' + str(int(parent_dir_no) + 1)
			parent_dir = "../training-data/Parent/"
			path = os.path.join(parent_dir, directory)
			os.mkdir(path)
			connection.commit()

			# Capture 12 training images
			# 0 => webcam
			# captureDevice => camera
			cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
			cv2.namedWindow("Capture image")
			img_counter = 0
			while True:
				ret, frame = cam.read()
				if not ret:
					print("failed to grab frame")
					break

				cv2.imshow("Capture image", frame)
				k = cv2.waitKey(1)

				if k%256 == 27 or img_counter > 12:			# ESC pressed or 12 images captured.
					print("Closing...")
					break

				elif k%256 == 32: 							# SPACE pressed
					img_name = path + '/opencv_frame_{}.png'.format(img_counter)
					cv2.imwrite(img_name, frame)
					print("{} written!".format(img_name))
					img_counter += 1
			cam.release()
			cv2.destroyAllWindows()

		except FileExistsError:
			# If the person is already registered.
			print('Seems that the parent already exists!')






	# =======================================================================

	elif choice == 'student':
		student_name = input("Enter student's name: ")
		phone_no = input("Enter your parent's phone no.: ")

		query = "select dir_no from surv_sys where phone_no='{}';".format(phone_no)
		cursor.execute(query)

		result = cursor.fetchall() 		# print(result) # [('1',)]
		result = int( result[0][0] )
		
		query = "update surv_sys set student_name='{}' where phone_no='{}';".format(student_name, phone_no)
		cursor.execute(query)

		# ===================================================================
		# Take 12 photos of that parent using a photoburst. =================
		# Store them in 's'+ str(student_dir_no)

		# Create directory
		print('student_dir_no: ', result+1)
		directory = 's' + str(result + 1)
		student_dir = "../training-data/Student/"
		path = os.path.join(student_dir, directory)

		try:
			os.mkdir(path)
			connection.commit()
			# Capture 12 training images
			cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) 	#captureDevice = camera
			cv2.namedWindow("Capture image")
			img_counter = 0
			while True:
				ret, frame = cam.read()
				if not ret:
					print("failed to grab frame")
					break

				cv2.imshow("Capture image", frame)
				k = cv2.waitKey(1)

				if k%256 == 27 or img_counter > 12:			# ESC pressed or 12 images captured.
					print("Closing...")
					break

				elif k%256 == 32: 							# SPACE pressed
					img_name = path + '/opencv_frame_{}.png'.format(img_counter)
					cv2.imwrite(img_name, frame)
					print("{} written!".format(img_name))
					img_counter += 1
			cam.release()
			cv2.destroyAllWindows()

		except FileExistsError:
			print('Seems that the student already exists!')
	

	connection.close()




def seek_entry(identity):
	# Data will be in two lists of same size: 
	# 	1. all the faces
	#	2. labels for each face
	print("Preparing data...")

	# print( prepare_training_data("D:/Project/training-data") )
	# Train the model based on student folder or parent folder. Take that as a parameter.
	faces, labels = DataPreparation().data_preparation("../training-data/" + identity)
	print("Data prepared")

	#print total faces and labels
	print("Total faces: ", len(faces))
	print("Total labels: ", len(labels))

	# Create model.
	face_recognizer = FaceRecogniser().create_model()


	# Train
	face_recognizer.train(faces, np.array(labels))


	# Prediction
	# Read from a file all the person's name and store it in subjects list.
	subjects = os.listdir("../training-data/" + identity)
	subjects.insert(0, "")
	#print('subjects', subjects)





	# Capture 12 training images
	cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) 	#captureDevice = camera
	cv2.namedWindow("Capture image")
	img_counter = 0
	while True:
		ret, frame = cam.read()
		if not ret:
			print("failed to grab frame")
			break

		cv2.imshow("Capture image", frame)
		k = cv2.waitKey(1)

		if k%256 == 27 or img_counter >= 1:			# ESC pressed or 12 images captured.
			print("Closing...")
			break

		elif k%256 == 32: 							# SPACE pressed
			img_name = 'opencv_frame_{}.png'.format(img_counter)
			cv2.imwrite(img_name, frame)
			print("{} written!".format(img_name))
			img_counter += 1
	cam.release()
	cv2.destroyAllWindows()

	test_img1 = cv2.imread('opencv_frame_{}.png'.format(img_counter-1))

	# Perform a prediction
	predicted_img, label_text = Prediction().predict(test_img1, subjects, face_recognizer, identity)

	#print( 'predicted_img: \n', predicted_img ) 

	if label_text == None:
		print('No matches found.')
	else:
		try:
			if predicted_img == None:
				print('Face did not match.')
			elif predicted_img.all() == None:
				print("No face detected. Can't recognize parent or child.")
			else:
				print("Prediction complete")
				print('Showing Image')
				cv2.imshow(subjects[label], predicted_img); cv2.waitKey(0); cv2.destroyAllWindows()
				print(':) ?')
		except:
			print("Prediction complete")

			print('Showing Image')
			cv2.imshow(label_text, predicted_img)
			cv2.waitKey(0)
			cv2.destroyAllWindows()

			#print(':) ?')