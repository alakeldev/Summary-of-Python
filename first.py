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


print(type( [1, 2, 3, 4, 5] ))    # list => List       in other Programming language known as Array

print(type( (1, 2, 3, 4, 5) ))    # tuple => tuple

print(type({"One" : 1 , "Two": 2, "Three": 3}))   # dict => Dictionary

print(type(2 == 2)) # bool => Boolean


"""
Variables:
- Just TO be Note That the Data is Stored Inside the Memory not inside the Variable, the Variable is only the label from this Data.

Syntax => [Variable Name] [Assignment Operator] [Value]

Example:
myVariable = "My Value"
print(myVariable)




- Source Code: Original Code You Write It in Computer (Python, C#, Java....).
- Translation: Converting Source Code Into Machine Language.
- Compilation: Translate Code Before The Run Time.
- Run-Time: The period App Take To Executing the Commands.
- Interpreted: Code Translated on the Fly during Execution.


Python is Dynamically typed language (because you can change the data in the run time without any issue)



if you want to know python keywords (Reserved Words) you can use as per below:
help("keywords")


"""

a, b, c = 2, 4, 6

print(a)
print(b)
print(c)

"""
Escape Sequances Characters:

\ b  => Back Space   

\ newline  =>   print("Hello \ 
                I'm \ 
                Alakel")

\ \ to print \ 

\ ' or \ "   => Escape double or single qoutes  

\ n it will make new line (Line feed)


\ r (Carriage Return)


\ t (Horizontal Tab)     // space but with tab button


\ xhh (Hex Value of the Character)

"""

print("Hello\bWorld")    # HellWorld

print("123456\rAbcd")    # Abcd56
print("123456\rAbcde")    # Abcde6
print("123456\rAbcdef")    # Abcdef



print("Hello\tWorld")    # Hello   World

print("\x41\x72")


"""
Concatenation:  Connect Two strings or more to make Long one string

- you Cannot Concatenate String With Number, it's only string with string

"""

msg = "My Name Is"
name = "Abdullah Alakel"

print(msg + " " + name)

full_msg = msg + " " + name

print(full_msg)


#--------------------------------------------

a = "First \
Hey \
Where"

b = "Momo \
Sasa \
Lolo"

print(a + "\n" + b)


"""
Strings:

myName = "Abdullah Alakel"   double qoute
myName1 = 'Abdullah Alakel'  single qoute

your can use double qoute or single qoute, also u can use double qoute inside single or single inside double without using scape charater


""" """ triple qoute it's using if you want your string to write it in more than one line and show the spaces and new lines without issues

also u can use the single qoute and double qoute inside it to make some words special without any issues or using scape charater

Example below
"""

myName = """Hello
How 
are You
?"""

print(myName)   #if you want to write the string in more than one line you need to use three or four or more lines for this string




"""
Strings Indexing and Slicing:

*All Data in python is Object
*Object contain Elemnts
*Every element has its own Index
*Python use Zero based Indexing
*use square Brackets to Access Element
*Enable Accessing parts of strings, tuple ,,, lists

"""
# Indexing (Access Single Item)

myString = "I Am Alakel"
print(myString[-3])   # k
print(myString[0])    # I
print(myString[2])    # A


# Slicing (Access Multiple Squence Items )
# [Start:End]    *****End Not Included
# [Start:End:Steps]   ** the steps by default are 1

print(myString[5:11])
print(myString[:6])  # if the start not specified so it will start from 0 by default 
print(myString[5:])  # if the end not specified so it will go to the end
print(myString[:])  # it will print the full data


print(myString[0::1])   ## it will print full data
print(myString[::1])    ## it will print full data

print(myString[::2])    ## it will take one and leave the next then take the next and leave the next..
print(myString[::3])    ## it will take one and leave the two next then take the one and leave the two next....


"""
#  len()     it's a build in function return the count items inside specific container
Example:
a = "I Love Python"
# print (len(a))    13  it's not indexing ,,,, the empty spaces it will count with len method

Strings Methods:

# String(), rstrip(), lstrip()

this Methods to remove the spaces inside the string by default value or you can provide specific characters to remove from the string

a = "     I Love Python      "
print(a.strip())       # it will remove the spaces right and left
print(a.rstrip())       # it will remove the spaces only on right side
print(a.lstrip())       # it will remove the spaces only on left side




a = "#####I Love Python######"
print(a.strip("#"))       # it will remove the # right and left
print(a.rstrip("#"))       # it will remove the # only on right side
print(a.lstrip("#"))       # it will remove the # only on left side


a = "@#@#@#@#I Love Python@#@#@#@#"
print(a.strip("@#"))       # it will remove the @# right and left
print(a.rstrip("@#"))       # it will remove the @# only on right side
print(a.lstrip("@#"))       # it will remove the @# only on left side





# title()
transfer the string to title (it will make each first letter from each word capital letter and the letter after numbers capital too)

b = "I love 2d Graphics and 3g Technology and python"

print(b.title())    // I Love 2D Graphics And 3G Technology And Python




# capitalize()
transfer the string as each first letter from each words will make it capital letter 

the difference between title and capitalize that the only first character will be capitalize and the rest is lower case


print(b.capitalize())  // I love 2d graphics and 3g technology and python



#zfill()   this method will tell that wants: width: and it's about how many zeroes want on the left

01
02
03
04
010
011
012
099
100
102
102



example: 
c, d, e = "1", "11", "111"

print(c)   # 1
print(d)    #11
print(e)    # 111

print(c.zfill(3)) #001    
print(d.zfill(3)) #011    
print(e.zfill(3)) #111    



c, d, e, f = "1", "11", "111", "1111"

print(c)   # 1
print(d)    #11
print(e)    # 111
print(f)    # 1111

print(c.zfill(4)) #0001    
print(d.zfill(4)) #0011    
print(e.zfill(4)) #0111    
print(f.zfill(4)) #1111    



upper(), lower()

g = "alakel"

print(g.upper())   # ALAKEL

i = "ALakel"
print(i.lower())   #alakel
"""

"""
Strings Methods part 2


- split(seprator, max-split)  
a = "I love Python and Javascript"
print(a.split())   # ['I', 'Love', 'Python', 'and', 'Javascript']     and it is a list by default seprator = space will be cut it

b = "I-Love-Python-and-Javascript"
print(b.split("-"))  # ['I', 'Love', 'Python', 'and', 'Javascript']     and it is a list the seprator = - will be cut it


c = "I-Love-Python-and-Javascript"
print(c.split("-", 2))  #['I', 'Love', 'Python-and-Javascript']    and it's a list the seperator is - and i want only 2 split then the rest will be in one element

print(c.split("-", 3))  #['I', 'Love', 'Python', 'and-Javascript'] 

- rsplit()
it's same of split but it will start from the right you can show in the below example:
c = "I-Love-Python-and-Javascript"
print(c.rsplit("-", 2))  #['I-Love-Python' ,'and', 'Javascript']

print(c.rsplit("-", 3))  #['I-Love' 'Python' ,'and', 'Javascript']





- center() it needs how many characters you want to return overall include the character of variable / the character that you want to add

e = "Samia"
print(e.center(9))   // spaces         Samia          
print(e.center(9, "#"))  // # Hashes    ##Samia##
print(e.center(15, "@"))  // @          @@@@@Samia@@@@@



- count("the word that i want to make search on it", "start index", "end index") it will return how many times the string available inside this variable
f = "I Love Python and Javascript because Javascript is easy"
print(f.count("Javascript"))    // 2   
print(f.count("Javascript", 0, 28 ))    // 1   




- swapcase()
it will swap letter from capital to lower and from lower to capital 
g = "I Love Python"   # i lOVE pYTHON
h = "i lOVE pYTHON"     # I Love Python


- startswith("the word/letter that i want to make search on it""start index", "end index")

i = "I Love Python"
print(i.startswith("I"))   # True
print(i.startswith("M"))   # False
print(i.startswith("P", 7, 12))   # True


- endswith("the word/letter that i want to make search on it""start index", "end index") always ends not icluded be attention 

i = "I Love Python"
print(i.endswith("n"))   # True
print(i.endswith("S"))   # False
print(i.endswith("e", 2, 6))   # True

"""