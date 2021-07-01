import cv2

import matplotlib.pyplot as plt

import os

import numpy as np

import mysql.connector as connector










#==============================================================================
#==============================================================================
# Face Detection

# Loading an image using OpenCV, it loads it into BGR color space by default. To show the colored image using 
# Matplotlib we have to convert it to RGB space. The following is a helper function to do exactly that:
def convertToRGB(img): 
	return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Function to detect face using OpenCV
def detect_face(img):
	# Convert the test image to gray scale as opencv face detector expects gray images
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
	#===================================================================
	# Load OpenCV face detector:
	
	# LBP
	# face_cascade = cv2.CascadeClassifier('D:/Project/lbpcascade/lbpcascade_frontalface.xml')

	# Haar classifier
	face_cascade = cv2.CascadeClassifier('D:/Project/haarcascades/haarcascade_frontalface_default.xml')
	

	# Detect multiscale images(some images may be closer to camera than others) 
	# Result : [] of faces ( type: np.ndarray: checked while debugging )
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);
	
	# No faces detected: Return None
	if (len(faces) == 0):
		return None, None

	#===================================================================
	# Print the number of faces found
	print('Faces found: ', len(faces))
	
	
	# Go over list of faces and draw them as rectangles on original colored
	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
	
	# Convert image to RGB and show image
	# plt.imshow(convertToRGB(img))
	
	# Under the assumption that there will be only one face, extract the face area
	x, y, w, h = faces[0]

	# Return only the face part of the image
	return gray[y:y+w, x:x+h], faces[0]


# test1 = cv2.imread('D:/Project/images/face3.jpg')
# detect_face( cv2.imread('D:/Project/images/face2.jpg') )
# for i in range(30):
# 	try:
# 		print('D:/Project/training-data/s1/opencv_frame_'+ str(i+1) +'.png')
# 		detect_face( cv2.imread('D:/Project/training-data/s2/opencv_frame_'+ str(i+1) +'.png') )
# 	except: print(i)










#==============================================================================
#==============================================================================
# Prepare Training Data

# Method definition
# This function will read all persons' training images, detect face from each image and will return two lists of 
# exactly same size, one list of faces and another list of labels for each face.
def prepare_training_data(data_folder_path):

	#------STEP-1--------
	# Get the directories (one directory for each subject) in data folder
	dirs = os.listdir(data_folder_path)
	#print(dirs)
	
	
	# List to hold all subject faces
	faces = []
	# List to hold labels for all subjects
	labels = []
	
	# Go through each directory and read images within it
	for dir_name in dirs:
		# Our subject directories start with letter 's' so ignore any non-relevant directories if any.
		if not dir_name.startswith("s"):
			continue;
			
		#------STEP-2--------
		# Extract label number of subject from dir_name format of dir name = slabel
		# So removing letter 's' from dir_name will give us label.
		label = int(dir_name.replace("s", ""))
		
		# build path of directory containing images for current subject sample subject_dir_path = "training-data/s1"
		subject_dir_path = data_folder_path + "/" + dir_name
	
		# Get the images names that are inside the given subject directory
		subject_images_names = os.listdir(subject_dir_path)
	
		count = 0
		# ------STEP-3--------
		# go through each image name, read image,detect face and add face to list of faces
		for image_name in subject_images_names:
			
			# ignore system files like .DS_Store
			if image_name.startswith("."):
				continue;
				
			# build image path
			# sample image path = training-data/s1/1.pgm
			image_path = subject_dir_path + "/" + image_name
			
			print(image_path)
			
			#read image
			image = cv2.imread(image_path)
		
			#display an image window to show the image 
			# cv2.imshow("Training on image...", image)
			# k = cv2.waitKey(1)

			#detect face
			face, rect = detect_face(image)

			#------STEP-4--------
			# we will ignore faces that are not detected
			if face is not None:
				count += 1
				#add face to list of faces
				faces.append(face)

				#add label for this face
				labels.append(label)

				# cv2.destroyAllWindows()
				# cv2.waitKey(1)
				# cv2.destroyAllWindows()

		print(count)
		
	return faces, labels


# Data will be in two lists of same size: 
# 	1. all the faces
#	2. labels for each face
print("Preparing data...")

# print( prepare_training_data("D:/Project/training-data") )

faces, labels = prepare_training_data("D:/Project/training-data")
print("Data prepared")

#print total faces and labels
print("Total faces: ", len(faces))
print("Total labels: ", len(labels))










#==============================================================================
#==============================================================================
# Create our LBPH face recognizer 
# The following line causes: 
# Error: cv2.cv2 has no attribute 'face'.
# No solution found for the current error.
# Possible cause: cv2 has moved 'face' from their original repo to some support package repo.
#face_recognizer = cv2.face.createLBPHFaceRecognizer()	

# The following works for creating an LBPH face recognizer.
face_recognizer = cv2.face_LBPHFaceRecognizer.create()

# Train our face recognizer of our training faces
face_recognizer.train(faces, np.array(labels))


# Function to draw rectangle on image according to given (x, y) coordinates and given width and heigh
def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
 
#function to draw text on give image starting from passed (x, y) coordinates. 
def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)




#==============================================================================
#==============================================================================
# Prediction:
# 		1. Recognize the person in image passed
#		2. Draws a rectangle + name around detected face.

def predict(test_img, subjects):
	# Make a copy of the image as we don't want to change original image
	img = test_img.copy()

	#detect face from the image
	face, rect = detect_face(img)

	#predict the image using our face recognizer 
	label = face_recognizer.predict(face)

	# Get name of respective label returned by face recognizer
	print('label= ', label)

	label_text = subjects[label[0]]
 

	#draw a rectangle around face detected
	draw_rectangle(img, rect)

	#draw name of predicted person
	draw_text(img, label_text, rect[0], rect[1]-5)
	 
	# print(img)
	return img

print("Predicting images...")

# Read from a file all the person's name and store it in subjects list.

# Set up the connection
connection = connector.connect(host="localhost",port=3306, user="root", passwd="root", database="surv_sys")
# Set up the cursor
cursor = connection.cursor()

subjects = ["", "Richik_Majumder", "Somhita_Majumder"]

# Load test images
# Positive cases
#test_img1 = cv2.imread('../test-data/s1/opencv_frame_0.png')
#test_img1 = cv2.imread('../test-data/s1/opencv_frame_3.png')

# Negative cases
#test_img1 = cv2.imread('C:/Users/RiM/Downloads/Wallpapers/red_mountains.jpg')
#test_img1 = cv2.imread('C:/Users/RiM/OneDrive/Pictures/Camera Roll/false_test.jpg')

test_img1 = cv2.imread('../test-data/s1/opencv_frame_0.png')

#perform a prediction
predicted_img1 = predict(test_img1, subjects)
#predicted_img2 = predict(test_img2)
print("Prediction complete")


#display both images
print('Showing Images')
cv2.imshow(subjects[1], predicted_img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.imshow(subjects[2], predicted_img2)

print(':( ?')