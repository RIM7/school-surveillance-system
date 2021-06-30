import mysql.connector as connector

# set up the connection
connection = connector.connect(host="localhost",port=3306, user="root", passwd="root", database="surv_sys")

# Set up the cursor
cursor = connection.cursor()
		

# student_name = input("Enter child's name : ")
# phone_no = input("Enter phone number : ")
# sql = "insert into [table-name](student_name, phone_no) values('{}','{}');".format(student_name, phone_no)



# Insert following data in table
# query = "insert into surv_sys(student_name, parent_name, phone_no) values('RiM', 'SoM', '7076405713');"
# cursor.execute( query );

query = "select * from surv_sys;"
cursor.execute( query )

print( cursor.fetchall() );

connection.close()