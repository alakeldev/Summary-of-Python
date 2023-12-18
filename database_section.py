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
# import sqlite3


# Create Database and connect
# db = sqlite3.connect("app.db")


##### Create The Tables and Fields
##### db.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER, user_id INTEGER)")
#### Close DB
#### db.close()




# Cursor => all operation in SQL done by the Cursor Not by the connection itself
# Commit => Save all changes

# Setting up the cursor it's better to create the cursor and use the cursor to create the tables 
# cr = db.cursor()

# cr.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER, name TEXT)")
# cr.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER, user_id INTEGER)")


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
# cr.execute("SELECT * FROM users")
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
# db.commit()

# close db
# db.close()


###########################################################
# Training on everything   IMPORTANT TO UNDERSTAND THIS TRAINING 

# import sqlite3

# def get_all_data():

    # try:
    
        # Connect to DB
        # db = sqlite3.connect("app.db")

        # print("Connected To DB Successfully")

        # Setting Up the Cursor
        # cr = db.cursor()

        # Fetch Data from DB
        # cr.execute("SELECT * FROM users")

        # Assign Data to Variable
        # result = cr.fetchone()

        # print(type(result))  ## Tuple


        # results = cr.fetchall()
        # print(type(results))  # List

        # print(results)      # [(1, 'Alakel'), (2, 'Khaled'), (3, 'Abdullah')]
        # print(results[0])   # (1, 'Alakel')
        # print(results[1])   # (2, 'Khaled')

        # print number of rows
        # print(f"Database Has {len(results)} Rows.")

        # printing message
        # print("Showing Data:")

        # Loop in results
    #     for row in results:
    #         print(f"UserID => {row[0]},", end=" ")

    #         print(f"Username => {row[1]}")

    # except sqlite3.Error as er:

    #     print(f"Error Reading Data {er}")


    # finally:    ## finaly will run what ever happened so it will run at the end
        # if (db):
            #close DB connection
            # db.close()

            # print("Connection to DB is closed")


# get_all_data()


###################################

## Update and Delete From DB


# import sqlite3


# db = sqlite3.connect("app.db")

# cr = db.cursor()


## Update Data    IMPORTANT
# cr.execute("UPDATE users SET name = 'Omar' WHERE user_id = 1")
# cr.execute("UPDATE users SET name = 'Alakel' WHERE user_id = 2")


# Delete Data     IMPORTANT
# cr.execute("DELETE from users WHERE user_id = 1")

# cr.execute("SELECT * FROM users")

# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())


# db.commit()

# db.close()


###################################


## Important information about Database

# Inserting data

# cr.execute("INSERT INTO skills (name, progress, user_id) VALUES ('JavaScript', '65', 2)")  ## Here to insert new data to the skills table
# cr.execute("INSERT INTO skills VALUES ('JavaScript', '65', 2)")  ## You Can write the above command shortcut


## to prevent an SQL injection attack
# my_tuple = ('JavaScript', '65', 1)
# cr.execute("INSERT INTO skills VALUES (?, ?, ?)", my_tuple)   # using place holder to prevent the SQL injection




## important information about Select and fetch the data
# cr.execute("SELECT * FROM skills ORDER BY user_id")    ## here will order the reult by user_id
# cr.execute("SELECT * FROM skills ORDER BY user_id asc")    ## here will order the reult by user_id ascending تصاعدي
# cr.execute("SELECT * FROM skills ORDER BY user_id desc")    ## here will order the reult by user_id descending تنازلي
# cr.execute("SELECT * FROM skills ORDER BY name")            ## ترتيب ابجدي 
# cr.execute("SELECT * FROM skills ORDER BY name asc")            ##  تصاعدي ترتيب ابجدي 
# cr.execute("SELECT * FROM skills ORDER BY name desc")            ##  تنازلي ترتيب ابجدي 
# cr.execute("SELECT * FROM skills ORDER BY name limit 2")            ##  it will return only two results
# cr.execute("SELECT * FROM skills ORDER BY name limit 3")            ##  it will return only Three results
# cr.execute("SELECT * FROM skills ORDER BY name limit 3 offset 2")            ## starting from the row 3, it will shift two rows and starting from the third



# cr.execute("SELECT * FROM skills WHERE user_id > 1") # Here results that user_id is bigger than 1   


# cr.execute("SELECT * FROM skills WHERE user_id IN (1, 2, 3)") # it will return for all user_ids 1, 2 and 3

# cr.execute("SELECT * FROM skills WHERE user_id NOT IN (1, 2, 3)") # it will return for all user_ids not equal 1, 2 and 3

