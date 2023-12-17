# DATABASE SECTION    IMPORTANT

# Database is a place were we can store data
# Database Organized Into tables(Users, Categories)
# Tables has Columns (ID, Username, Password)
# There is many types of Database (MongoDB, MySql, SQLIte)
# SQL stand for Structured Query Language
# SQLITE => Can run in Memory or in a single file
# You Can Browse File With https://sqlitebrowser.org
# Data Inside Database has type (Text, Integer, Date)


# print("-------------------------------------------------")
# print("-------------------------------------------------")

## Connect
## Execute
## Close

#Importing SQLite Module
import sqlite3


# Create Database and connect
db = sqlite3.connect("app.db")


##### Create The Tables and Fields
##### db.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER, user_id INTEGER)")
#### Close DB
#### db.close()




# Cursor => all operation in SQL done by the Cursor Not by the connection itself
# Commit => Save all changes

# Setting up the cursor it's better to create the cursor and use the cursor to create the tables 
cr = db.cursor()

cr.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER, name TEXT)")
cr.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER, user_id INTEGER)")


# Inserting Data
# cr.execute("INSERT INTO users(user_id, name) VALUES(1, 'Alakel')")
# cr.execute("INSERT INTO users(user_id, name) VALUES(2, 'Khaled')")
# cr.execute("INSERT INTO users(user_id, name) VALUES(3, 'Abdullah')")




# Below a small example with a list of names that make a loop on it and add all the names with giving them an id using enumerate method and adding them to the DB
# my_list = ["Alakel", "Abdullah", "Almama", "Ali", "SOSO", "FOFO", "Samyah", "LOLO"]

# for key, user in enumerate(my_list):
#     cr.execute(f"INSERT INTO users(user_id, name) VALUES({key + 1}, '{user}')")







######## How to fetch and retreive the ata from the Database
# fetchone => returns a single record or None if no more rows are available
# fetchall => fetches all the rows of a qurey result. It returns all the rows as a list of tuples. an empty list is returned if there is no record to fetch
# fetchmany(size) => 

#fetch data
cr.execute("SELECT * FROM users")
# cr.execute("SELECT name FROM users")
# cr.execute("SELECT user_id, name FROM users")

# - Fetchone
# print(cr.fetchone())  ## (1, 'Alakel')
# print(cr.fetchone())  ## (2, 'Khaled')
# print(cr.fetchone())  ## (3, 'Abdullah')
# print(cr.fetchone())  ## None

# - Fetchall
# print(cr.fetchall())   ## [(1, 'Alakel'), (2, 'Khaled'), (3, 'Abdullah')]


# - Fetchmany(how many rows want)
# print(cr.fetchmany(2))   # [(1, 'Alakel'), (2, 'Khaled')]




# Save (Commit the Changes)
db.commit()

# close db
db.close()