# Import required modules
import csv
import sqlite3

# Connecting to the geeks database
connection = sqlite3.connect('user.db')

# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()

# Table Definition
create_table = '''CREATE TABLE IF NOT EXISTS user(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                firstname TEXT NOT NULL,
                lastname TEXT NOT NULL,
                department TEXT NOT NULL,
                location TEXT NOT NULL);
                '''

# Creating the table into our
# database
cursor.execute(create_table)

# Opening the person-records.csv file
file = open('user.csv')

# Reading the contents of the
# person-records.csv file
contents = csv.reader(file, delimiter=',')
# for row in csv_reader_object:
#         print(row)

# SQL query to insert data into the
# person table
insert_records = "INSERT INTO user (id, username, email, firstname, lastname, department, location) VALUES(?, ?, ?, ?, ?, ?, ?)"

# Importing the contents of the file
# into our person table
cursor.executemany(insert_records, contents)

# SQL query to retrieve all data from
# the person table To verify that the
# data of the csv file has been successfully
# inserted into the table
select_all = "SELECT * FROM user"
rows = cursor.execute(select_all).fetchall()

# Output to the console screen
for r in rows:
    print(r)

# Commiting the changes
connection.commit()

# closing the database connection
