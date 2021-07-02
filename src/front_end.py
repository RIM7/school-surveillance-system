from tkinter import *;  from tkinter import font;

from util import register_person, seek_entry



def clicked():
	pass

def sel(self):
	pass

#def __init__(self):

#self.root = Tk();
root = Tk()
root.geometry('800x500')
root.resizable(0, 0); 
# root.iconbitmap(getcwd() + '\\AEC_logo.ico')
root.title('Student Survelliance System')

#Create canvas1 to take inputs.
canvas1 = Canvas(root, bg = 'white', width=800)
canvas1.pack(side='left', fill = 'both')

def moved(event): 
	canvas1.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))

canvas1.bind("<Motion>", moved)
tag = canvas1.create_text(10, 10, text="", anchor="nw")



#canvas1 contents==========================================================================================================

Label(canvas1,text='What do you want to do:',font=('Courier',12,'bold'),bg='peach puff3', justify='left').place(x=280,y=50)


try:
	register_as_a_parent = Button(canvas1, text='Register as a parent', 
										font=('Courier',12,'bold'), 
										bg='white', width=50, 
										command= lambda: register_person('parent')) 

	register_as_a_parent.place(x=150, y=100)



	register_as_a_student = Button(canvas1, text='Register as a student', 
							font=('Courier',12,'bold'), 
							bg='white', 
							width=50, 
							command=lambda: register_person('student'))

	register_as_a_student.place(x=150, y=150)



	seek_entry_parent = Button(canvas1, text='Enter as a parent', 
										font=('Courier',12,'bold'), 
										bg='white', 
										width=50, 
										command= lambda: seek_entry('Parent') )

	seek_entry_parent.place(x=150, y=200)



	seek_entry_student = Button(canvas1, text='Enter as a student', 
										font=('Courier',12,'bold'), 
										bg='white', 
										width=50, 
										command= lambda: seek_entry('Student') )

	seek_entry_student.place(x=150, y=250)


	exit = Button(canvas1, text='Exit', font=('Courier',12,'bold'), bg='white', width=50, command = root.destroy )
	exit.place(x=150, y=300)

	root.mainloop()


except: 
	pass