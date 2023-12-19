# Advanced Lessons:

# __name__ => is a built in variable in python language
# __main__ => is the value of __name__ variable in direct execution file Method

# Execution Methods:
# - Directly => execute the python file using the command line
# - From Import => Import the code from file to another file

# In some cases you want to know if you are using a module method as import or you use the original python file

# In direct Mode Python assin a value "__main__" to the built in variable __name__ in the background

# print("show me everywhere")

# if __name__ == __main__:
#     print ("Show me When file is running directly")

# else:
#     print("This file Not running Directly")


# print("Show me everywhere")


####################################################################

# Timing your code with timeit Module

# Timeit: Get execution time of code by runnigng 1 Million time and give you the minimal time it used to preformance by testing all functionality
# timeit(stmt, setup, timer, number)
# timeit(pass, pass, default, 1.000.000) default values

# stmt: code statement you want to measure the execution time
# setup: Setup done before the code execution(import module or anything)
# timer: the timer value
# number: how many execution that will run



# import timeit

# print(dir(timeit))  ## the important here is repeat and timeit methods

# print(timeit.timeit("'Alakel' * 1000"))


# name = "Alakel"
# print(name * 1000)

# print(timeit.timeit("name = 'Alakel'; name * 1000"))  ## Here in one statement you declare a variable name then it * 1000




# another example:
# print(random.randint(0, 50))

# print(timeit.timeit(stmt="random.randint(0, 50)", setup="import random")) # Here we put the value of setup to import the random module before stmt start working


# timeit.repeat() here in our example below, i told that make the full timeit 4 times so will check 1.000.000 then give me the minimum result then will make another time check 1.000.000 then give me the minimum time then....total 4 times
# print(timeit.repeat(stmt="random.randint(0, 50)", setup="import random", repeat=4)) # so it will return a list and inside this list 4 results 


####################################################################
####################################################################
####################################################################

# Add logging to your code 
# - print out to console or file
# - print logs of what happens


# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

# name => Logging Module Give it to the Default Logger.

# Basic Config
# - Level => level of severity
# - filename => File Name and Execution
# - mode => Mode of the file a => append
# - format => Format For the log Message


# getLogger => return a logger with the specified name 


# import logging

# print(dir(logging))

# logging.basicConfig(filename="my_app.log", filemode="a", format=" (%(asctime)s) => | %(name)s | %(levelname)s => '%(message)s' ")

# logging.critical("This is Critical Message")




# logging.basicConfig(filename="my_app.log", filemode="a", format=" (%(asctime)s) | %(name)s | %(levelname)s => '%(message)s' ")


# logging.error("This is Error Message")



# logging.info("This is Info Message")

# logging.debug("This is debug Message")



# logging.basicConfig(filename="my_app.log", 
#                     filemode="a", 
#                     format=" (%(asctime)s) | %(name)s | %(levelname)s => '%(message)s' ", 
#                     datefmt="%d- %B - %Y, %H:%M:%S")





## here to change the logger from the root (default) to a specific value that i want as per below 
# my_logger = logging.getLogger("Alakel")


# my_logger.warning("This is waning Message")



####################################################################
####################################################################
########################################################################################################################################
####################################################################
########################################################################################################################################
####################################################################
########################################################################################################################################
####################################################################
########################################################################################################################################
####################################################################
####################################################################

# Generate Random Serial Numbers    IMPORTANT TO GENERATE RANDOM NUMBER IMPORTANT IMPORTANT

import string
import random

# print(string.digits)      # 0123456789
# print(string.ascii_letters)   # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz
# print(string.ascii_uppercase)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ

def make_serial(count):
    all_chars = string.ascii_letters + string.digits
    # print(all_chars)

    chars_count = len(all_chars)
    # print(chars_count)   # 62 Chars

    serial_list = []

    while count > 0:

        random_number = random.randint(0, chars_count - 1) # here get a number from 0 to 61

        random_character = all_chars[random_number]

        serial_list.append(random_character)

        count -= 1

    print("".join(serial_list))



make_serial(30)




# another simple example to understand that python starting cound 0 based indexing so you must be note that put a less a number than your taget here:

# test = "1234"

# print(random.randint(0, 3))
# print(test[0])
# print(test[1])