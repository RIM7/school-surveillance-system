import cv2
import numpy as np


from util import register_person, seek_entry



if __name__=='__main__':

	# seek_entry('parent')

	while True:
		choice = input('Enter your choice:\n\t1. Register yourself.\n\t2. Seek entry.\n\t3. Exit.\n')
		if choice == '3':
			print('Program end.')
			break

		elif choice == '1':
			parent_or_student = input('Choose your identity:\n\t1. Register as a parent.\n\t2. Register as a student.\n\t3. Exit.\n')

			if parent_or_student == '1':
				register_person('parent')
			elif parent_or_student == '2':
				register_person('student')
			else:
				break

		elif choice == '2':
			parent_or_student = input('Choose your identity:\n\t1. Enter as a parent.\n\t2. Enter as a student.\n\t3. Exit.\n')

			if parent_or_student == '1':
				seek_entry('Parent')
			elif parent_or_student == '2':
				seek_entry('Student')
			else:
				break

		else:
			break