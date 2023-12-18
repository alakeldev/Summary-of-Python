import sqlite3

#Create Database and connect
db = sqlite3.connect("skills_app.db")

# Setting Up the Cursor
cr = db.cursor()

# Create the skills table if not exists
# cr.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER, user_id INTEGER)")

# Method to save changes and close the database
def commit_and_close():
    """ Commit changes and close connection with database """
    #save (commit) changes
    db.commit()
    # close Database
    db.close()
    print("Database connection closed")             # only to check if it's working properly
    

# my user ID
uid = 2




# Message to show when the application run
input_message = """
What do You want to do ?
"s" => show all skills
"a" => add new skill
"d" => delete skill
"u" => update skill progress
"q" => quite the app
choose the option:
"""

# input for the user to take the input and save it inside a variable
user_input = input(input_message).strip().lower()

# Command List
commands_list = ["s", "a", "d", "u", "q"]


# Defined the methods
def show_skills():
    
    cr.execute(f"SELECT * FROM skills WHERE user_id='{uid}'")

    results = cr.fetchall()

    print(f"You Have {len(results)} skills.")

    if len(results) > 0:

        print("Below Your Skills With Progress: ")

    for row in results:

        print(f"Skill => {row[0]},", end=" ")
        print(f"Progress => {row[1]}%")

    commit_and_close()





def add_skill():
    sk = input("Write Skill Name: ").strip().capitalize()

    prog = input("Write Skill Progress: ").strip()

    cr.execute(f"INSERT INTO skills(name, progress, user_id) VALUES('{sk}', '{prog}', '{uid}')")

    commit_and_close()

def delete_skill():
    sk = input("Write Skill Name: ").strip().capitalize()

    cr.execute(f"DELETE FROM skills WHERE name = '{sk}' AND user_id = '{uid}'")

    commit_and_close()

def update_skill():
    print("update skill progress")

    commit_and_close()



# check if the command is exists
if user_input in commands_list:
    # print(f"Commands found {user_input}")        # only to check if it's working properly

    if user_input == "s":
        show_skills()
    elif user_input == "a":
        add_skill()
    elif user_input == "d":
        delete_skill()
    elif user_input == "u":
        update_skill()
    else:
        print("Close the App")
        commit_and_close()


else:
    print(f"Sorry This Command \"{user_input}\" not found ")