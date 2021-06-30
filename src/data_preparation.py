import cv2
import os

from face_detection import FaceDetection


#==============================================================================
#==============================================================================
# Prepare Training Data

class DataPreparation:

	# Method definition
	# This function will read all persons' training images, detect face from each image and will return two lists of 
	# exactly same size, one list of faces and another list of labels for each face.
	def data_preparation(self, data_folder_path):

		#------STEP-1--------
		# Get the directories (one directory for each subject) in data folder
		self.dirs = os.listdir(data_folder_path)
		#print(self.dirs)
		
		
		# List to hold all subject faces
		self.faces = []
		# List to hold labels for all subjects
		self.labels = []
		
		# Go through each directory and read images within it
		for dir_name in self.dirs:
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
		
			# count = 0
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
				face, rect, no_of_faces = FaceDetection().detect_face(image)


				#------STEP-4--------
				# We will not process images with multiple faces
				if no_of_faces > 1:
					print("Can't process the image. Multiple faces detected. Skipping.")

				# We will ignore faces that are not detected
				elif face is not None:
					# count += 1
					#add face to list of faces
					self.faces.append(face)

					#add label for this face
					self.labels.append(label)

					# cv2.destroyAllWindows()
					# cv2.waitKey(1)
					# cv2.destroyAllWindows()

			# print(count)
			
		return self.faces, self.labels