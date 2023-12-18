import sqlite3

input_message = """
What do You want to do ?
"s" => show all skills
"a" => add new skill
"d" => delete skill
"u" => update skill progress
"q" => quite the app
choose the option:
"""


user_input = input(input_message).strip().lower()

# Command List
commands_list = ["s", "a", "d", "u", "q"]


# Defined the methods
def show_skills():
    print("Show Skills") 

def add_skill():
    print("add skill")

def delete_skill():
    print("delete skill")

def update_skill():
    print("update skill progress")

# check if the command is exists
if user_input in commands_list:
    print(f"Commands found {user_input}")

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


else:
    print(f"Sorry This Command \"{user_input}\" not found ")