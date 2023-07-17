"""
what is Python?
It's Programming language that can do anything.
Free and Open Source (use it free and also update it in future too).
Iterpreted (Code will process in the run time and you gonna see the output direct) no need to make compiled to see the output.
Interactive (You gonna see the output inside the terminal)


Why Python:
- Easy to Install (inside your software to can use it).
- Clean and Easy (easy to learn and clean to type it no need ; only in special cases).
- Debugging is Easy (Debugger Created with Python).
- Cross Platfrom (you can develop in through all softwares such as: windows-Mac-Linux).
- Expressive (So you can understand it with easy in english).
- OOP (Object Oriented Programming).
- Integrated (You can Build App through two languages integrate more than language python with another programming language).
- Support Module and Packages (You can add Module and Package to you software to add it to app)
- Large Set of Libraries and Plugins.
- Memory Management (Garbage Collection: if you have any variable or data forget it inside the memory with python these useless Variables
and data will remove it and collect it together to make the memory empty and clean).
- Multi Purpos (it has many use cases and very good language).
- Has Great Community(its document very good and you can find it easy).
- Growing very fast.
- Yo can switch careers with the basic knowledge.


What Can I Do With Python?
- Web Development (Django, Flask).
- Games (pyGame).
- DeskTop Apps (PyGUI, Tkinter).
- Hacking - Network.
- Machine Learning & Data Science.
- AI & Robots.
- Automation(Testing and Automate specific task).
- Web Scrapping (Harvest) Website to show last prices for coins ,gold, cypto.
- Andriod Games (with Frameworks).


Some Apps Created With Python:
- Disqus
- Instagram
- Spotify
- Dropbox
- Uber

Some Companies using Python:
- Facebook
- Google
- Netflix

Best IDEs:
- VS-code
- PyCharm


Comment in python:  Ctrl + # (Shortcut)
"""

print("Hello Python, my first application")
print("Hello Django")

# the use case of ; inside python if you want to write more than order in oneline
print("Hello Python"); print("Hello Django")



"""
Dealing with Data:
in Each application we have:
- Code
- Data

* The code is the lines you write to manage and deal with data.
* Structure the Data we need to Categorize {Num, String, Boolean,.....}.

* Data is stored on Computer Memory.
* We use Variable to refer to this Data.
* Variable Not Conatining the data. Its only refer to its Location Inside the memory.
* Code is using the data to preform operation [Add, Edit, Delete, Update,....]

"""

"""
All Data in Python is Object.

type()    // it's build in function it will showing the type of this data

"""

print(type(10))   # int => Integer
print(type(-10))   # int => Integer
print(type(-103))   # int => Integer


print(type(101.96))   # float => floating point number
print(type(-101.96))   # float => floating point number
print(type(1.9556656656))   # float => floating point number


print(type("Alakel"))    # str => String


print(type( [1, 2, 3, 4, 5] ))    # list => List

print(type( (1, 2, 3, 4, 5) ))    # tuple => tuple

print(type({"One" : 1 , "Two": 2, "Three": 3}))   # dict => Dictionary

print(type(2 == 2)) # bool => Boolean
