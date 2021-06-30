import mysql.connector as connector

# set up the connection
connection = connector.connect(host="localhost",port=3306, user="root", passwd="root", database="surv_sys")

# Set up the cursor
cursor = connection.cursor()

# Fetch all tables available in the database.
cursor.execute("show tables");

# List out all tables.
list_of_tables = cursor.fetchall()


#====================================================================
#====================================================================
# Check whether the table 'surv_sys' is present or not.
flag_surv_sys = 0
flag_currently_present_children = 0
flag_currently_present_parent = 0

for i in list_of_tables:
	# print(i)
	if i == ('surv_sys',):
		flag_surv_sys = 1
		# Generate log
		print("'surv_sys' exists.")

	if i == ('currently_present_children',):
		flag_currently_present_children = 1
		# Generate log
		print("'currently_present_children' exists.")

	if i == ('currently_present_parent',):
		flag_currently_present_parent = 1
		# Generate log
		print("'currently_present_parent' exists.")

	if flag_surv_sys == 1 and flag_currently_present_children == 1 and flag_currently_present_parent == 1:
		break



# Create table if not exists
# For surv_sys
if flag_surv_sys == 0:
	# Generate log
	print('Creating table surv_sys...')

	# Execute create table query
	query = "create table surv_sys( student_name varchar(100), parent_name varchar(100), phone_no varchar(10) );"
	cursor.execute( query )

	# Generate log
	print('Table surv_sys created...')


# For currently_present_children
if flag_currently_present_children == 0:
	# Generate log
	print('Creating table currently_present_children...')

	# Execute create table query
	query = "create table currently_present_children( student_name varchar(100), phone_no varchar(10) );"
	cursor.execute( query )

	# Generate log
	print('Table currently_present_children created...')


# For currently_present_parent
if flag_currently_present_parent == 0:
	# Generate log
	print('Creating table currently_present_parent...')

	# Execute create table query
	query = "create table currently_present_parent( parent_name varchar(100), phone_no varchar(10) );"
	cursor.execute( query )

	# Generate log
	print('Table currently_present_parent created...')


connection.close()
