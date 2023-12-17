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
print(c.split("-", 2))  #['I', 'Love', 'Python-and-Javascript']    and it's a list the seperator is - and i want only 2 split then
the rest will be in one element

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



- count("the word that i want to make search on it", "start index", "end index") it will return how many times the string 
available inside this variable
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





- index()

a= "I Love Python"
print(a.index(substring that wants to search for, start, end))

print(a.index("P"))  # index number 7
print(a.index("P", 0, 10)   # index number 7
print(a.index("P", 0, 5)   # Error substring not found (will stop the code)


- find(substring that wants to search for, start, end)

the difference between find and index ,,,, the find method will return -1 if no find the value but the index will return error 
and stop the code

c= "I Love Python"
print(c.find("P"))  # index number 7
print(c.find("P", 0, 10)   # index number 7
print(c.find("P", 0, 5)   # -1





- rjust(width, fill char)   , ljust(width, fill char)

c = "Alakel"
print(c.rjust(10))      //       Alakel
print(c.rjust(10, "@"))  // @@@@Alakel

c = "Alakel"
print(c.ljust(10))      //Alakel    
print(c.ljust(10, "@"))  //Alake@@@@




- splitlines()  return all lines inside list

# e = """ #First line
#Second Line
#Third Line """ 

# print(e.splilines())    // ['First Line', 'Second Line', 'Third Line']
# print(type(e.splilines()))    // list


# another way to return list from long string:

# f = "First Line\nSecond Line\nThird Line"
#print(f.splitlines())    // ['First Line', 'Second Line', 'Third Line']





# expandtabs(number of tabes you want (tabe button))

g = "Hello\tWorl\tI\tLove\tPython"
print(g)

print(g.expandtabs(10))



one = "I Love Python And 3G"

print(one.istitle())    #True, each first letter in each word capital letter and after the number capital letter

two = "I Love Python And 3g"   
print(two.istitle())       # False, because the letter after number is small letter



three = " "  
print(three.isspace())   # True

four = "i love python"
five = "I Love Python"

print(four.islower())  # True
print(five.islower())   # False


seven = "Abdullah Alakel"
eight = "Abdullah Alakel100"
nine = "Abdullah--Alakel100"
print(seven.isidentifier())   # True
print(eight.isidentifier())     # True
print(nine.isidentifier())      # False because no - inside Identifier


x = "AaaaaBbbbbb"
print(x.isalpha())     # True  because the value is from Aa to Zz

y = "AaaaaBbbbbb11"
print(y.isalpha())  # False because of the number inside the value




u = "AaaaaBbbbbb"
print(u.isalnum())     # True  because the value is from Aa to Zz and all number 0 to 9

z = "AaaaaBbbbbb11"
print(z.isalnum())  # True because  because the value is from Aa to Zz and all number 0 to 9





# - replace(old value, new value, count to say how many times we want to replace it)

u = "Hello One Two Three One One"

print(u.replace("One", "1"))      # Hello 1 Two Three 1 1
print(u.replace("One", "1", 1))   # Hello 1 Two Three One One



# - join(Iterable on object) to make loop on it 

myList = ["Abdullah", "Khaled", "Alakel"]
print("-".join(myList))  # Abdullah-Khaled-Alakel
print(" ".join(myList)) # Abdullah Khaled Alakel
print(",".join(myList)) # Abdullah,Khaled,Alakel
print(type(",".join(myList)))  # string

#"""


# strings formatting    (OLD WAY) 

name = "Abdullah"
age = 25
rank = 10

print("My Name is: " + name)
# print("My Name is: " + name + "and My Age is: " + age)  # type error
print("My name Is %s" % name)
print("My name Is %s and My Age is: %d" % (name, age))    # %s (placeholder string)   %d(plavegolder digit"number")
print("My name Is %s and My Age is: %d and My Rank is: %f" % (name, age, rank)) # %s (placeholder string)   %d(placeholder => digit"number" 
#  %f (placeholder => Floating point number))



# another Example:
n = "Alakel"
l = "Python"
y = 6 

print("Iam %s I Love %s since %d years" % (n, l, y))


# control the floating point number how many numbers after the ,
myNumber = 10
print("My Number is: %.2f" % myNumber)   # .2f it will show only two numbers after the ,


# Truncate String cut from string things i want to delete from it and keep that i want:

myLongString = "Hello People I love You All And I love Python too"
print("Message is: %s" %myLongString) # Message is: Hello People I love You All And I love Python too
print("Message is: %.5s" %myLongString) # Message is: Hello


#------------------------------------------------------------------------------------------------------------


# String Formatting    (New Ways to Learn)

name = "Abdullah"
age = 25
rank = 10


print("My name Is {}".format("Abdullah")) # .format("")
print("My name Is {} and My Age is: {}".format(name, age))  # .format(variables)
print("My name Is {:s} and My Age is: {:d} and My Rank is: {:f}".format(name, age, rank))  # {:s}   {:d}   {:f}
print("My name Is {:s} and My Age is: {:d} and My Rank is: {:.2f}".format(name, age, rank))  # {:s}   {:d}   {:.2f}
#  %f (placeholder => Floating point number))



# Truncate String (new Ways to Learn)

myLongString = "Hello People I love You All And I love Python too"
print("Message is: {}".format(myLongString)) # Message is: Hello People I love You All And I love Python too
print("Message is: {:.5s}".format(myLongString)) # Message is: Hello
print("Message is: {:.12s}".format(myLongString)) # Message is: Hello People


# Format Money

myMoney = 5235400255122

print("My Money In Bank Is: {:_d}".format(myMoney))
print("My Money In Bank Is: {:,d}".format(myMoney))


# Rearrange Items

a, b, c = "One", "Two", "Three"

print("Hello {} {} {}".format(a, b, c))   #Hello One Two Three
print("Hello {1} {2} {0}".format(a, b, c))   #Hello Two Three One
print("Hello {2} {0} {1}".format(a, b, c))   #Hello Three One Two


x, y, z = 10, 20, 30
print("Hello {} {} {}".format(x, y, z))     #Hello 10 20 30
print("Hello {1:d} {2:d} {0:d}".format(x, y, z))    #Hello 20 30 10
print("Hello {2:.2f} {0:.1f} {1:.4f}".format(x, y, z))   #Hello 30.00 10.0 20.0000




# Format in Version 3.6 and above:  Very Important way to follow the formatting here similair to JS

myName = "Alakel"
myAge = 25

print(f"My Name Is : {myName} and My Age is : {myAge}")


# Please Visit Website :  pyformat.info   to check the format old and new ways in details 

#------------------------------------------------------------------------------------------------------------




# Numbers


# Integer:
print(type(1))
print(type(100))
print(type(10))
print(type(-10))
print(type(-2021))
print(type(0))


# Float:
print(type(1.500))
print(type(10.99))
print(type(-11.20))
print(type(0.91))



# Complex:
print(type(5+6j))    # it contain two parts (real part, imaginary part)


myComplexNumber = 5+6j

print("Real Part Is: {}".format(myComplexNumber.real))   # // 5.0
print("Real Part Is: {}".format(myComplexNumber.imag))   # // 6.0

# You Can Convert From Int to Float or Complex
# You Can Convert From Float to Int or Complex
# You Can NOT Convert Complex To Any Type

# Examples
print(100)   #100
print(float(100))   # 100.0
print(complex(100))  #(100+0j)

print(10.50)   # 10.5
print(int(10.50)) # 10
print(complex(10.50)) #(10.5+0j)


print(10+9j)
# print(int(10+9j))   # Error Cannot Convert Complex Number to Integer


#------------------------------------------------------------------------------------------------------------

#Arithmetic Operators

# Addition
print(20 + 20)   # 40
print(10 + 10)   # 20
print(1.1 + 2.3)   # 3.4


# Subtraction
print(60 - 30)    # 30
print (-30 - 20)   # -50
print (-30 - -20)  # -10
print(5.66 - 3.44) # 2.22


# Muliplication
print(10 * 3)  # 30
print(5 + 10 * 100)  # 1005
print((5 + 10) * 100) # 1500


# Division
print(100 / 20) # 5.0
print(int(100 / 20)) # 5



# Modulus
print(8 % 2) # 0
print(9 % 2) # 1
print(20 % 5) # 0
print(22 % 5) # 2


# Exponent
print(2 ** 5)    # 32      (2 * 2 * 2 * 2 * 2)
print(5 ** 4)    # 625        (5 * 5 * 5 * 5)


# Floor Division

print (100 // 20)   # 5
print (110 // 20)   # 5
print (119 // 20)   # 5
print (120 // 20)   # 6
print (130 // 20)   # 6
print (139 // 20)   # 6
print (140 // 20)   # 7



#------------------------------------------------------------------------------------------------------------

# Intro to Lists:

# Lists it's same array in other programming languages but it's not array because if you want array u must import modul to use the array in py

# - List items are enclosed in square brackets
# - List items are ordered, to use index to access item
# - List items are Mutable (Add - Delete - Edit)
# - List items is not unique
# - List can have Different Data Types


myAwesomeList = ["One", "Two", "One", 1, 100.5, True]

print(myAwesomeList)   # ['One', 'Two', 'One', 1, 100.5, True]
print(myAwesomeList[1])  # Two
print(type(myAwesomeList[1]))  # string
print(myAwesomeList[-1])  # True
print(myAwesomeList[-3])    # 1


print(myAwesomeList[1:4])   # ["Two", "One", 1]                 # Ends not Included
print(myAwesomeList[:4])    # if start empty it will start from index 0    # ['One', 'Two', 'One', 1]
print(myAwesomeList[1:])    # if end empty it will continue to the last    # ['Two', 'One', 1, 100.5, True]


print(myAwesomeList[::1])  # it will show the full list because the step is default
print(myAwesomeList[::2])  # it will take element and leave the next then take one and leave the next


# print(myAwesomeList[150])    # List index out of range

print(myAwesomeList)

myAwesomeList[1] = 2        # edit on my original list
myAwesomeList[-1] = False    # edit on my original list
# myAwesomeList[0:2] =  []     # here no items available it's empty
# myAwesomeList[0:3] =  []     # here no items available it's empty
# myAwesomeList[0:3] =  ["A", "B", "C"]     # add new values inside the list   # ['A', 'B', 'C', 1, 100.5, False]
myAwesomeList[0:3] =  ["A"]     #['A', 1, 100.5, False]     # remove three items and put instead of them only one item without any issues
print(myAwesomeList)




# Lists Methods

# - Append()     when you want to add new item or more to the list

myFriends = ["Alakel", "Abdullah", "Sawaf"]
myOldFriends = ["Ahmad", "Abode", "Sami"]
myFriends.append("MaMa")
myFriends.append(100)
myFriends.append(152.112)
myFriends.append(True)
myFriends.append(myOldFriends)


print(myFriends)
print(myFriends[2])  # Sawaf
print(myFriends[6]) # True
print(myFriends[7]) # ['Ahmad', 'Abode', 'Sami']
print(myFriends[7][1]) # Abode
print(myFriends[7][2]) # Sami


# - extend()         the different between append and extend, the extend can concatenate two list and extend the list example below:

a = [1, 2, 3]
b = ["a", "b", "c"]

a.extend(b)

print(a)    # [1, 2, 3, 'a', 'b', 'c']

c = ["One", "Two"]

a.extend(c)

print(a)   # [1, 2, 3, 'a', 'b', 'c', 'One', 'Two']



# - remove()      it will remove specific element fron your list

y = [1, 2, 3, 4, 5, "Alakel", True, "Alakel", "Alakel"]

y.remove("Alakel")

print(y)   # [1, 2, 3, 4, 5, True, 'Alakel', 'Alakel']  it will remove the first item same "Alakel"will face it in its way and keep the rest



# - sort()  it accepts numbers or letters (string) only without mixing
# if you include string with numbers it will show an error so it's important to note that

y = [1, 2, 100, 120, -10, 17, 29]

y.sort()

print(y)   # [-10, 1, 2, 17, 29, 100, 120]

y.sort(reverse=True)

print(y) #[120, 100, 29, 17, 2, 1, -10]



# - reverse()    it accepts mixing between numbers and string because it's only reverse without sorting

z = [10, 1, 9, 80, 100, "Alakel", 100]

z.reverse()

print(z)  # [100, 'Alakel', 100, 80, 9, 1, 10]



# - clear()   it will clear the list (remove all items from the list)

a = [1, 2, 3, 4]

a.clear()
print(a)    # []



# - copy()   when you want to take a copy from the list then you don't care what happened/changed with the main 
# list because ur copy will be the same   (Shallow Copy)

b = [1, 2, 3, 4]

c = b.copy()    # return Shallow copy

print(b)    # main list    [1, 2, 3, 4]
print(c)    # copied list  [1, 2, 3, 4]

b.append(5)


print(b)    # main list    [1, 2, 3, 4, 5]
print(c)    # copied list  [1, 2, 3, 4]


# - count()   it will count the element how many times show inside my list 

d = [1, 2, 3, 4, 3, 9 , 10, 1 ,2 , 1]

print(d.count(1))   # 3    the number one inside the list show three times


# - index()   it will show the first index going to face with its way


e = ["Alakel", "Abdullah", "Alakel", "Ahmad", "Abdulrahman", "Mama"]

print(e.index("Alakel"))   # 0
print(e.index("Abdullah"))   # 1
# print(e.index("Sami"))   # Error is not in list


# - insert((insert object before INDEX), Object)   

f = [1, 2, 3, 4 ,5 , "A", "B"]
f.insert(0, "Test")
f.insert(-1, "FAFA")
print(f)  # ['Test', 1, 2, 3, 4, 5, 'A', 'FAFA', 'B']


# - pop()

g = [1, 2, 3, 4, 5, "A", "B"]

# print(g.pop(2))   # 3
# print(g.pop(-1))   # B
# print(g.pop(-3))   # 5


#------------------------------------------------------------------------------------------------------------

# Tuple Intro:

# 1- Tuple items are enclosed in parentheses           ex: myTuple = ("Abdullah", "Alakel")
# 2- You can remove the parentheses if you want        ex : myTuple = "Abdullah", "Alakel"
# 3- Tuple are ordered, you can use index to access the items    

myTuple = (1, 2, 3, 4, 5)
print(myTuple[-1])

# 4- Tuple are Immutable => You Can NOT Add or Delete

# myNewTuple = (1, 2, 3, 4, 5)

# myNewTuple[2] = "Three"

# print(myNewTuple)   # Error Tuple does not support item assignment

# 5- Tuple items is not Unique    (Same List)
# 6- Tuple can have different data types

myNewTuple = ("Alakel", "Alakel", 1, 2, 3, 10.3, True)

print(myNewTuple[1])
print(myNewTuple[-1])


# 7- Operators used in strings and lists available in tuples too



# Tuple Methods:

# tuple with one Element how we can say this is a tuple with one element Example:

myTuple1 = ("Alakel",)
myTuple2 = "Alakel",

print(myTuple1)
print(myTuple2)
print(type(myTuple1))   # tuple
print(type(myTuple2))   # tuple
print(len(myTuple1))   # 1
print(len(myTuple2))   # 1




# Tuple Concatenation

a = (1, 2, 3, 4)
b = (5, 6)

c = a + ("A", "B", True) + b 

print(c)   # (1, 2, 3, 4, 'A', 'B', True, 5, 6)




# Tuple, List , String Repeat *

myString = "Alakel"
myList = [1, 2]
myTuple = ("A", "B")

print(myString * 6)   # AlakelAlakelAlakelAlakelAlakelAlakel
print(myList * 6)   # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
print(myTuple * 6)  # ('A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B')



# Methods:

# count()   to check the element how many times repeat inside the tuple

a = (1, 3, 7, 8, 2, 6 ,5 , 8)

print(a.count(8))   # 2   


# index()

b = (1, 3, 7, 8, 2, 6 , 5)

print("The Position Of Index Is: {:d}".format(b.index(8)))   # 3
print(f"The Position of Index Is: {b.index(8)}")   # 3



# Tuple Destruct

a = ("A", "B", "C")

x, y, z = a   

print(x)   #A
print(y)    #B
print(z)    #C


# another Example:
b = ("F", "G", 4, "D")

# t, m ,n = b    // Too many Values to unpack Error

# if you want to escape one value inside the tupe you follow as per below and skip with _

t, m, _, n = b

print(t)
print(m)
print(n)

#------------------------------------------------------------------------------------------------------------

# Set  Intro:

# 1- Set Items are Enclosed in Curly Braces    ex: mySet = {}
# 2- Set Items are NOT ordered and Not Indexed


mySetOne = {"Alakel", "Abdullah", 100}
print(mySetOne)

# print(mySetOne[1])   # Error
# 3- Set Indexing and Slicing can NOT be Done

mySetTwo = {1, 2, 3, 4, 5, 6}
# print(mySetTwo[0:2])   # Error


# 4- Set Has Only Immutable Data Types (Numbers, Strings , Tuples) List and Dict are NOT

# mySetThree = {"Abdullah", 10, 10.5, True, [1, 2, 3]}  # The issue because of the list inside the set
# print(mySetThree)    #ERROR unhashable type (hashing mechanism in computer science allow to search on objects inside computer memory)

mySetFour = {"Abdullah", 10, 10.5, True,(1, 2, 3)}   # here everthing is ok because of using tuple instead of list

print(mySetFour) 



# 5- Set items are UNIQUE

mySetFive = {1, 2, "Alakel", "Alakel", 1, "Abdullah"}
print(mySetFive)  # {'Alakel', 1, 2, 'Abdullah'}  the items repeated will ignored and will show it only one time what ever times repeated





# Set Methods:

# clear()     it will remove all elements from the set

a = {1, 2, 3}
a.clear()
print(a)


# union()     it make union with two sets and more

b = {"One", "Two", "Three"}
c = {"1", "2", "3"}
x = {"WeWe", "FeFe"}
print(b | c)
print(b.union(c, x))


# add()   it will add element to the set - it will accept one argument only

d = {1, 2, 3, 4}

d.add(5)
d.add(6)
print(d)


# copy()    Shallow Copy

e = {1, 2, 3, 4}
f = e.copy()

print(e)  # {1, 2, 3, 4}
print(f)  # {1, 2, 3, 4}

e.add(6)

print(e) #{1, 2, 3, 4, 6}
print(f) #{1, 2, 3, 4}



# remove()    it will remove element from the set

g = {1, 2, 3, 4}
g.remove(1)

print(g)   #{2, 3, 4}

# g.remove(7)   # ERROR the keyerror because element not found inside the set



# discard()   the different between remove and discard if we give element not inside the set it will not return an Error same remove method

h = {1, 2, 3, 4}
h.discard(1)

print(h)   #{2, 3, 4}

h.discard(7)   # It will not return ERROR even the element not inside the set items



# pop()

i = {"A", True, 1, 2, 3, 4, 5}
print(i.pop())   # it will return random element from the set




# update()    update the set with the union of itself and others

j = {1, 2, 3}
k = {1, "A", "B", 2}

j.update(["HTML", "CSS", "JS"])    # update the j set with list
j.update(k)         # update the j set with other set k 

print(j)  # {1, 2, 3, 'B', 'CSS', 'A', 'HTML', 'JS'}   it will ignore the repeat items and will take them only one time




# difference()  if you want to know the difference between two sets, it will appear/show the elements inside the first set and not available
# inside the second set 

a = {1, 2, 3, 4}
b = {1, 2, "Alakel", "Abdullah"}

print(a) # {1, 2, 3, 4}
print(a.difference(b))  # {3, 4}

# you can get same result from the difference method as per below
print(a - b)   # {3, 4}



# difference_update()   it will return the difference and it will update the original set with these difference values

c = {1, 2, 3, 4}
d = {1, 2, "Alakel", "Abdullah"}

c.difference_update(d)   

print(c)   # {3, 4}


print("-------------------------------------------------")

# intersection()  it will return the items that showing in both sets

e = {1, 2, 3, 4, "X"}
f = {"Alakel", "X", 2}

print(e)   # {'X', 1, 2, 3, 4}

print(e.intersection(f))     # {'X', 2}

print(e)  # {'X', 1, 2, 3, 4}


print("-------------------------------------------------")


# intersection_update()   it will reitn the items that showing in both sets and it will update the original set with this value

g = {1, 2, 3, 4,"Alakel", "X"}
h = {"Alakel", "X", 2}

print(g)    # {1, 'Alakel', 3, 2, 4, 'X'}
g.intersection_update(h)                       # g & h
print(g)    # {'Alakel', 2, 'X'}


print("-------------------------------------------------")


# symmertice_difference()     it will return the items that not showing in both sets

i = {1, 2, 3, 4, 5, "X"}
j = {"Alakel", "Abdullah", 1, 2, 4}

print(i)    # {1, 2, 3, 4, 5, 'X'}

print(i.symmetric_difference(j))   # i ^ j        # {'Abdullah', 3, 'Alakel', 5, 'X'}

print(i)     # {1, 2, 3, 4, 5, 'X'}



print("-------------------------------------------------")

# symmertice_difference_update#()   it will return the items that not showing in both sets and update with this value the original set

k = {1, 2, 3, 4, 5, "X"}
l = {"Alakel", "Abdullah", 1, 2, 4}

print(k)   # {1, 2, 3, 4, 5, 'X'}

k.symmetric_difference_update(l)

print(k)   # {'Abdullah', 3, 5, 'X', 'Alakel'}


print("-------------------------------------------------")


# Special set Methods that return True Or False (Boolean value)


# issuperset()

a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {1, 2, 3, 4, 5}

print(a.issuperset(b))  # True why? because it will check the elements inside b if all b set elements same inside a set 
# so it will return True 

print(a.issuperset(c)) # False why? becuase it will check on all elements in c set if all c set elements are not same a set element 
# so it will return False


print("-------------------------------------------------")


# issubset()

d = {1, 2, 3, 4}
e = {1, 2, 3}

f = {1, 2, 3, 4, 5}

print(d.issubset(e))  # False why? becuase it wil check on d set if all elements are same inside e set element so it will return True

print(d.issubset(f)) # True why? because it will check on d set if all elements are same inside f set elements so it will return True 



print("-------------------------------------------------")


# isdisjoint()

g = {1, 2, 3, 4}
h = {1, 2, 3}
i = {10, 11, 12}

print(g.isdisjoint(h))  # False becuase both sets are have 1, 2, 3 

print(g.isdisjoint(i))   # True becuase 10, 11, 12 are not inside the original set elements so they are disjoint 

print("-------------------------------------------------")


#------------------------------------------------------------------------------------------------------------

# Dictionary intro:

# 1- Dict items are enclosed in curly braces
# 2- Dict items are contains Key : Value
# 3- Dict Key need to be Immutable => (Number, String, Tuple) List not Allowed
# 4- Dict Value Can be any Data Type
# 5- Dict Key Need To be Unique
# 6- Dict Is not Ordered, You can access it element with its key
user = {
    "name": "Alakel",
    "age": 25,
    "country": "Syria",
    (1, 2, 3, 4): "MyTuple",
    1 : "Baby",
    "skills" : ["HTML", "CSS", "Python"],
    "rating": 10.2,
    # "name": "Abdullah"  # it will update the key and take the last key with same name
}

print(user)

print(user["country"])    #Syria
print(user.get("country"))   #Syria

print(user.keys())   # dict_keys(['name', 'age', 'country', (1, 2, 3, 4), 1, 'skills', 'rating'])
print(user.values())   #dict_values(['Alakel', 25, 'Syria', 'MyTuple', 'Baby', ['HTML', 'CSS', 'Python'], 10.2])


print("-------------------------------------------------")


# Two-Dimentional Dictionary (Nested Dictionary)

languages = {
    "One": {
        "name": "HTML",
        "progress": "100%"
    },
    "Two": {
        "name": "CSS",
        "progress": "90%"
    },
    "Three": {
        "name": "JS",
        "progress": "90%"
    }
    }

print(languages)

print(languages["One"])   #{'name': 'HTML', 'progress': '100%'}
print(languages["Three"])   #{'name': 'JS', 'progress': '90%'}

print(languages["Three"]["progress"])    #90%
print(languages["Three"]["name"])    #JS


# Dictionary Length
print(len(languages))   # 3   it means the languages dict has three elements
print(len(languages["Two"]))   # 2  it means that Two dictionary how many elemnts has inside it



# Create Dictionary From Variables

frameworkOne = {
    "name": "React.js",
    "progress": "80%"
}

frameworkTwo = {
    "name": "Angular",
    "progress": "60%"
}

frameworkThree = {
    "name": "Vuejs",
    "progress": "90%"
}

allFramework = {
    "One": frameworkOne,
    "Two": frameworkTwo,
    "Three": frameworkThree
}

print(allFramework)

print("-------------------------------------------------")


# Dictionary Methods:


# - clear()   clear all elements inside the dictionary

user = {
    "name": "Alakel",
    "age": 25
}

print(user)   #{'name': 'Alakel', 'age': 25}

user.clear()

print(user)   #{}

print("-------------------------------------------------")


# - update()   it allows to add new elements to ur dictionary 

member = {
    "name": "Alakel",
    "age": 26
}

print(member)   # {'name': 'Alakel', 'age': 26}

member["country"] = "Syria"

print(member)   # {'name': 'Alakel', 'age': 26, 'country': 'Syria'}   # without using update() method


member.update({"gender": "Male"})

print(member)   # {'name': 'Alakel', 'age': 26, 'country': 'Syria', 'gender': 'Male'}   # with using update method




# - copy()        Shallow Copy the new copy will not effect if you add or edit the original Dictionary

main = {
    "name": "Alakel"
}

b = main.copy()

print(b)  # {'name': 'Alakel'}

main.update({"country": "Germany"})

print(main)   # {'name': 'Alakel', 'country': 'Germany'}
print(b)   # {'name': 'Alakel'}



# - keys() + values()


print(main.keys())    # dict_keys(['name', 'country'])
print(main.values())    # dict_values(['Alakel', 'Germany'])

print("-------------------------------------------------")


# - setdefault()

user = {
    "name": "Alakel",   
}

print(user)   # {'name': 'Alakel'}
print(user.setdefault("name", "Abdullah")) # Alakel  it appears here alakel because it will search for the key name value inside the dict
# if it finds the value or this key it will return it from the dict if not find it so it will set the new value "Abdullah" as a value to this key
# also if you didn't provide a value so it will return a None data type   print(user.setdefault("age"))
print(user)   # {'name': 'Alakel'}


print("-------------------------------------------------")


# - popitem()    it will return the last item added to the dictionary 

member = {
    "name" : "Alakel",
    "skill": "PS4"
}

print(member)   # {'name': 'Alakel', 'skill': 'PS4'}
print(member.popitem())   # ('skill', 'PS4')

member.update({"age": 26})

print(member.popitem())   # ('age', 26)



print("-------------------------------------------------")


# - items()   here the most main point that all future change on the dictionary will effect the items and it will show on it 

view = {
    "name": "Alakel",
    "skill": "PS5"
}

allItems = view.items()

print(view) # {'name': 'Alakel', 'skill': 'PS5'}

view["age"] = 26

print(allItems)    # dict_items([('name', 'Alakel'), ('skill', 'PS5'), ('age', 26)])    BIG LIST AND CONATIN TUPLES


print("-------------------------------------------------")



# fromkeys()    to make dictionary from keys and vlaues

a = ("MyKeyOne", "MyKeyTwo", "MyKeyThree")

b = "X"

print(dict.fromkeys(a, b))   # {'MyKeyOne': 'X', 'MyKeyTwo': 'X', 'MyKeyThree': 'X'}    Dictionary

print("-------------------------------------------------")


#------------------------------------------------------------------------------------------------------------


# Boolean

# 1- In Programming you need to know if you code output is True or False
# 2- Boolean Values are two constant Objects False or True

name = " "
print(name.isspace())  # True

print(100 > 200)   # False

print(100 > 100)    # False

print(100 > 50)    # True

print("-------------------------------------------------")


# bool() build in function return True if the arguement is True value else False  Examples:


# True Values
print(bool("Alakel"))
print(bool(100))
print(bool(10.5))
print(bool(True))
print(bool([1, 2, 3, 4]))

print("-------------------------------------------------")

# False Values
print(bool(""))
print(bool(''))
print(bool(0))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(False))
print(bool(None))


print("-------------------------------------------------")


# Boolean Operators:
# - and  

age = 36
country = "Syria"
rank = 10

print(age > 16)   # True
print(country == "Syria")    # True

print(age > 16 and country == "Syria" and rank > 5)    # True
print(age > 16 and country == "UAE" and rank > 5)    # False

print("-------------------------------------------------")

# - or

print(age > 40 or country == "Germany") # False
print(age > 40 or country == "Germany" or rank > 10) # False
print(age > 40 or country == "Syria" or rank > 10) # True

print("-------------------------------------------------")

# not

print(age > 16)  # True
print(not age > 16)  # not True = False



print("-------------------------------------------------")

# Assignment Operators

# =
# +=
# -= 
# *=
# /=
# **=
# %=
# //=
#-------------------------

x = 10   # assign a value to a variable
y = 20   # assign a value to a variable

#x = x + y  
#print(x) # 30
#x += y 
#print(x) # 50



# x = x - y   # -10

x -= y   # -10

print(x)


print("-------------------------------------------------")


# Comparison Operators:

# [ == ] Equal
# [ != ] Not Equal



print(100 == 100)  # true
print(100 == 200)   # False
print(100 == 100.0)   # True

print("-------------------------------------------------")

print(100 != 100)  # False
print(100 != 200)  # True
print(100 != 100.0) # False

print("-------------------------------------------------")




# [ > ] Greater Than
# [ < ] Less than 


print(100 > 100)  # False
print(100 > 200)   # False
print(100 > 100.0)   # False
print(100 > 40)   # True

print("-------------------------------------------------")

print(100 < 100)  # False
print(100 < 200)   # True
print(100 < 100.0)   # False
print(100 < 40)   # False

print("-------------------------------------------------")

# [ >= ] Greater Than Or Equal
# [ <= ] less Than Or Equal


print(100 >= 100)  # True
print(100 >= 200)   # False
print(100 >= 100.0)   # True
print(100 >= 40)    # True


print("-------------------------------------------------")


print(100 <= 100)  # True
print(100 <=200)   # True
print(100 <= 100.0)   # True
print(100 <= 40)   # False


#------------------------------------------------------------------------------------------------------------
print("-------------------------------------------------")

# Type Conversion:

# str()

a = 10
print(type(a)) # int
print(type(str(a)))    # str


print("-------------------------------------------------")

# tuple()        this method it needs an element can make iteration on him (Loop on the element)

c = "Alakel"   # string
d = [1, 2, 3, 4, 5]   # list
e = {"A", "B", "C"}  # set
f = {"A": 1, "B": 2}  # Dictionary

print(tuple(c))   # ('A', 'l', 'a', 'k', 'e', 'l')
print(tuple(d))   # (1, 2, 3, 4, 5)
print(tuple(e))   # ('B', 'C', 'A')
print(tuple(f))   # ('A', 'B')
# print(tuple(500))   # Error Object Int is not Iterable no Iteration on it


print("-------------------------------------------------")


# list()

c = "Alakel"   # string
d = (1, 2, 3, 4, 5)   # tuple
e = {"A", "B", "C"}  # set
f = {"A": 1, "B": 2}  # Dictionary



print(list(c))   #['A', 'l', 'a', 'k', 'e', 'l']
print(list(d))   # [1, 2, 3, 4, 5]
print(list(e))   # ['A', 'C', 'B']
print(list(f))   # ['A', 'B']


print("-------------------------------------------------")
print("-------------------------------------------------")



# set()


c = "Alakel"   # string
d = (1, 2, 3, 4, 5)   # tuple
e = ["A", "B", "C"]  # list
f = {"A": 1, "B": 2}  # Dictionary



print(set(c))   # {'k', 'e', 'l', 'A', 'a'}
print(set(d))   # {1, 2, 3, 4, 5}
print(set(e))   # {'B', 'A', 'C'}
print(set(f))   # {'B', 'A'}



print("-------------------------------------------------")
print("-------------------------------------------------")


# Dict()

# c = "Alakel"   # string       it cause ERROR
# d = (1, 2, 3, 4, 5)   # tuple    it Cause ERROR to avoid the error u must make nested tuples inside the main tuple as per below
d = (("A", 1), ("B", 2), ("C", 3))
# e = ["A", "B", "C"]  # list  it cause Error to avoid the error u must make nested lists inside the main list as per below 
e = [["one", 1], ["Two", 2], ["Three", 3]]

# f = {{"A", 1}, {"B", 2}}  # Set Error even we follow tuple and list way because it's unhashable type so not accept to make set a dictionary



# print(dict(c))   # ERROR String
print(dict(d))   # {'A': 1, 'B': 2, 'C': 3}
print(dict(e))   # {'one': 1, 'Two': 2, 'Three': 3}
# print(dict(f))   # ERROR Set


print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------

# User Input

#fName = input("What's Your First Name?")
#mName = input("What's Your Middle Name?")
#lName = input("What's Your Last Name?")
# We use Strip method if user make spaces in his name before or after so it will remove by this method
# we use capitalize method if use mixed letter with capital and small letter so this method will return the first letter only capitalize
#fName = fName.strip().capitalize()
#mName = mName.strip().capitalize()
#lName = lName.strip().capitalize()

#print(f"Hello {fName} {mName:.1s} {lName}, You Are Welcome.") # we use here :.1s for middle name to return only the first letter from the name



print("-------------------------------------------------")



# Practical Slice Email

# email = "Abdullah_alakel@alakel.org"
# print(email[:email.index("@")])

# theName = input("What's Your Name?").strip().capitalize()
# theEmail = input("What's Your Email?").strip()

# theUsername = theEmail[:theEmail.index("@")]
# theDomain = theEmail[theEmail.index("@") + 1 :]

# print(f"Your Name Is {theName} Your Email Is {theEmail}")
# print(f"Your Username Is {theUsername} \nYour Domain Is {theDomain}")


print("-------------------------------------------------")


# Practical your Age full Details:

#age = int(input("What is Your Age ? ").strip())

# Age in All Time Types

#months = age * 12
#weeks = months * 4
#days = age * 365
#hours = days * 24
#minutes = hours * 60
#seconds = minutes * 60

#print("You Lived Alomst: ")
#print(f"{months} Months.")
#print(f"{weeks} Weeks.")
#print(f"{days:,} Days.")
#print(f"{hours:,} Hours.")
#print(f"{minutes:,} Minutes.")
#print(f"{seconds:,} Seconds.")


print("-------------------------------------------------")

# Control Flow If , Elif, Else    (Make Decisions)   Example to understand it


#uName = "Abdullah"
#cName = "Python"
#cPrice = 100
#uCountry = "KSA"

#if uCountry == "Syria":
#    print(f"Hello {uName} You Are From {uCountry}. \nThe Course '{cName}' Price Is: {cPrice - 80} $")

#elif uCountry == "UAE":
#    print(f"Hello {uName} You Are From {uCountry}. \nThe Course '{cName}' Price Is: {cPrice - 50} $")

#elif uCountry == "KSA":
#    print(f"Hello {uName} You Are From {uCountry}. \nThe Course '{cName}' Price Is: {cPrice - 40} $")

#else:
#    print(f"Hello {uName} You Are From {uCountry} . \nThe Course '{cName}' Price Is: {cPrice - 30} $")



print("-------------------------------------------------")
print("-------------------------------------------------")


# Nested If

#uName = "Abdullah"
#student = "Yes"
#cName = "Python"
#cPrice = 100
#uCountry = "Syria"


#if uCountry == "Syria" or uCountry == "UAE" or uCountry == "Qatar":
#    if student == "Yes":
#        print(f"Hello {uName} You Are From {uCountry} And You Are a Student Too.")
#        print(f"The Course '{cName}' Price Is: {cPrice - 80} $")
#    else:
#        print(f"Hello {uName} You Are From {uCountry}.")
#        print(f"The Course '{cName}' Price Is: {cPrice - 60} $")
#elif uCountry == "KSA" or uCountry == "Iraq":
#    print(f"Hello {uName} You Are From {uCountry}. \nThe Course '{cName}' Price Is: {cPrice - 50} $")

#else:
#    print(f"Hello {uName} You Are From {uCountry}. \nThe Course '{cName}' Price Is: {cPrice - 20} $")


print("-------------------------------------------------")


# Ternary Conditional operator:

#country = "Syria"

#if country == "Syria": print(f"The Weather in {country} is 15")
#elif country == "UAE": print(f"The Weather in {country} is 30")
#else: print("Country Is Not Available")

print("-------------------------------------------------")


# Short If:

#showRate = 18
#age = 16

#if age < showRate :
#    print("The Show Is not for Your Age")
#else :
#   print("The Show Is for Your age and enjoy it")



#Syntax:

# Condition if true | if condition | else | condition if false
#print("The Show Is not for Your Age" if age < showRate else "The Show Is for Your age and enjoy it")



print("-------------------------------------------------")
print("-------------------------------------------------")


# Practical Your Age Full Details 
#print("#" * 80)
#print(" You can write the first letter only from type unit ".center(80,"#"))
#print("#" * 80)

#age = input("Enter Your Age Here: ").strip()

#unitTime = input("Please Choose Time Unit: Months, Weeks, Days \n").strip().lower()


#months = int(age) * 12
#weeks = months * 4
#days = int(age) * 365

#if unitTime == "months" or unitTime == "m":
#    print("Months Choosed")
#    print(f"You Lived For {months:,} Months. ")
#elif unitTime == "weeks" or unitTime == "w":
#    print("Your Choosed Weeks")
#    print(f"Your Lived For {weeks:,} Weeks. ")
#elif unitTime == "days" or unitTime == "d":
#    print("You Choosed Days")
#    print(f"Your Lived For {days:,} Days. ")


print("-------------------------------------------------")
print("-------------------------------------------------")


# Membership Operators:
# In
# Not In

# - String
name = "Alakel"
print("a" in name)   # True
print("A" in name)   # True
print("K" in name)   # False

print("-------------------------------------------------")

# - List

friends = ["Alakel", "Abdullah", "Samir"]

print("Alakel" in friends)  # True
print("SASA" in friends)   # False

print("Abdullah" not in friends)  # False
print("SASA" not in friends) # True


print("-------------------------------------------------")

# Using in and not in with conditions:

countriesOne = ["Syria", "UAE", "KSA", "Kuwait"]
countriesDisc1 = 80
countriesTwo = ["USA", "Germany"]
countriesDisc2 = 50

myCountry = "USA"

if myCountry in countriesOne:
    print(f"Hello You have a Discount: ${countriesDisc1}")

elif myCountry in countriesTwo:
    print(f"Hello You have a Discount: ${countriesDisc2}")

else: 
    print("Sorry You Have No Discount")


print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------


# Practical Membership Control Example,,,,Advanced Example:

# Names list that can access the app:

#members = ["Alakel", "Abdullah"]

#login

#name = input("Enter Your Name: ").strip().capitalize()



#if name in members :

#    print(f"Welcome {name}, Happy To See Your Again")

#    option = input("Delete or Update your Name: ").strip().capitalize()

#    if option == "Update":
#        theNewName = input("Write Your New Name: ").strip().capitalize()
#        members[members.index(name)] = theNewName

#        print("Name Updated Without Issues! =) ")
#        print(members)


#    elif option == "Delete":
#        members.remove(name)
#        print("The Name Deleted Without Issues! =)")

#       print(members)

#    else:

#        print("Your Choose Wrong Option, please choose between delete and update")

#else:

#    message = input("You are Not From the members, You Want to Add Your Self: Y, N ?").strip().capitalize()

#    if message == "Y" or message == "Yes":

#        print("Added Successfully")

#        members.append(name)

#        print(members)

#    else:

#        print("You Are Not Added To our Members")


print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

# While  Loop:             the code inside it, will run till the condition change to false
# Syntax


# While Conidition_Is_True
# Code Will Run


# a = 0
# while a < 15:

#     print(a)
#     a += 1

# print("Loop Finished")


## here it will not run the code inside while becuase it's already false and while not run if it's false
#while False :
#    print("Will not print")



# Training on While Loop:

#myFriends = ["Alakel", "Abdullah","Almama", "Sami", "Maher", "Fatin", "Elfie", "Layan"]


# print(len(myFriends))    # List Length

# without the loop
print(myFriends[0])
print(myFriends[1])
print(myFriends[2])
print(myFriends[3])
print(myFriends[4])
print(myFriends[5])
print(myFriends[6])
print(myFriends[7])

print("-------------------------------------------------")
print("-------------------------------------------------")

# With while loop
# zfill() method we use it to put a 0 number before the number 1 as we put its value as 2 characters
# str() method to change it to string to we can use zfull method on it 
a = 0 
while a < len(myFriends) :
    print(f"#{str(a + 1).zfill(2)} {myFriends[a]}")
    a += 1

else:
    print("All Friends Printed.")


print("-------------------------------------------------")
print("-------------------------------------------------")




# Simple Bookmark Manage     While Training   Advanced Important

#myFavouriteWebsites = []

#maxWebsites = 5

#while maxWebsites > 0 :

#    website = input("Please Enter Your Website: ")

#   myFavouriteWebsites.append(f"https://{website.strip().lower()}")

#    maxWebsites -= 1

#    print(f"Website Added, still pending {maxWebsites}")

#    print(myFavouriteWebsites)

#else:
#    print("BookMarks Is Full, Sorry You Cannot Add More!")


#if len(myFavouriteWebsites) > 0 :
    
#    myFavouriteWebsites.sort()

#    index = 0

#    print("Printing the BookMarks")

#    while index < len(myFavouriteWebsites) :
        
#        print(myFavouriteWebsites[index])

#        index += 1

print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------



# loop while Advanced Example:    Simple Password Guess:

#myTries = 4

#myPassword = "123456@"

#inputPassword = input("Please Write Your Password: ")

#while inputPassword != myPassword :

#    myTries -= 1

#    print(f"Wrong Password Try Again please, Remain { 'last' if myTries == 0 else myTries } Tries")

#    inputPassword = input("Please Write Your Password: ")

#    if myTries == 0:

#        print("You Finished All Password Tries")

#        break

#else:
#    print("Correct Password")


print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------

# Loop : For

#syntax:
# for item in iterable_object :
    # block of code

myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in myNumbers :

    #print(number * 10)

    if number % 2 == 0 :   # even,
        print(f"The Number {number} is Even")
    
    else :
        print(f"The Number {number} is Odd.")

else:   # it's not same else of while, the else inside for it's only refer that the loop finished 

    print("The Loop finished")

print("-------------------------------------------------")

#Another Example on string (loop)

myName = "Alakel"

for letter in myName:
    print(f"[ {letter.upper()} ]")


print("-------------------------------------------------")




# For Loop Training:

#myRange = range(1, 100)       # range() built in function that generate for a bunch of numbers that you put the range between 1, 100

#for number in myRange:
#    print(number)

# Dictionary

mySkills = {
    "HTML": "90%",
    "CSS": "70%",
    "JS": "60%",
    "Python": "80%",
    "React": "90%"
}

#print(mySkills["JS"])
#print(mySkills.get("Python"))


for skill in mySkills:
    #print(skill)    # print only keys

    print(f"My Progress In IT {skill} is: {mySkills[skill]}")     # this way to print the values of the keys 
    print(f"My Progress In IT {skill} is: {mySkills.get(skill)}")  # this way to print the values of the keys 
    print("-------------------------------------------------")



print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------


# For Loop   (Nested loop)

people = ["Alakel", "Abdullah", "Khaled", "Mama", "MiMi"]

skills = ["HTML", "CSS", "Js"]

for name in people :    # Outer Loop

    print(f"{name} Skills Is: ")

    for skill in skills:     # Inner Loop
        print(f"# {skill}")



print("-------------------------------------------------")
print("-------------------------------------------------")
print("-------------------------------------------------")
print("-------------------------------------------------")

# Simple Example to UnderStand Important for Nested For Loop:

employers = {
    "Alakel": {
        "html": "70%",
        "css": "40%",
        "JS": "50%"

    },
    "Abdullah": {
            "HTML": "10%",
        "css": "20%",
        "JS": "30%"
    },
    "Akel": {
            "html": "90%",
        "css": "70%",
        "Js": "100%"
    }
    
}

for employer in employers:     
    print(f"Skills and Progress for {employer} is: ")      ##employer will return the key of the main dictionary

    for skill in employers[employer] :    ## employers[employer] will return the keys of the nested dictionary
        print(f"# {skill.upper()}: {employers[employer][skill]}")  # employers[employer][skill] will return the values of nested dictionary


print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------

# Break, Continue, Pass

#myNumbers = [1, 2, 3, 4, 5, 6, 10, 15 , 17 ,19]

#for number in myNumbers :
    #Continue

    #if number == 10:     ## it will stop current iteration/loop and continue after it 
    #    continue


    #Break

    #if number == 10:     ## it will exit/break the iteration/loop
        
    #    break

    #Pass

    #if number == 10:

    #    pass  # main purpose is when you are testing the code and at somepoint u want to skio/pass the empty if conditions or any code u want

    # print(number)

print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------

# Advanced Dictionary Loop:

myNewSkills = {
    "HTML": "80%",
    "Css": "70%",
    "python": "50%",
    "Js": "60%"
}

# First Way to get the result and get loop on keys and values of the dictionary:

#print(myNewSkills.items())

#for skill in myNewSkills:
#    print(f"{skill} => {myNewSkills[skill]}")




# the Second Way to get the result and get loop on keys and values of the dictionary:

#for skillKey, skillValue in myNewSkills.items():
#    print(f"{skillKey} => {skillValue}")




# Advanced Example:   Important to UnderStand Nested Loop with important notes to understand

myUltimateSkills = {
    "HTML": {
        "Main": "80%",
        "Pugjs": "70%"
    },
    "CSS": {
        "Main": "90%",
        "Sass": "50%"
    }
}


for main_key, main_value in myUltimateSkills.items() :
    print(f"{main_key} Progress Is: ")
    for child_dic_key, child_dic_value in main_value.items() :
        print(f"{child_dic_key}  #{child_dic_value}")


print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------


# Function and Returns:   the Most Important Section:
# 1- Function is a reusable block of code to do a task
# 2- Function Run When You Call it
# 3- Function Accept Elements to Deal with Called [Parameters]
# 4- Function Can Do Specific task without return Data
# 5- Function Can Return Data after run Finished
# 6- Function Create to Prevent DRY    Don't Repeat Your Self
# 7- Function accenpt elements when you call it [Arguments]
# 8- There is a Built-in Functions and user defined Functions
# 9- Function is for All team and all Apps


def function_name():

    print("Hello World From Inside Function")


function_name()    # Here you call the function


print("-------------------------------------------------")


def function_name_Two():
    
    return "Hello World From Inside Function Two"


function_name_Two()    # Here you call the function but it will not show anything on terminal

print(function_name_Two()) # here You Call the function and you print it because inside the function it's return a value not print it

print("-------------------------------------------------")

#------------------------------------------------------------------------------------------------------------

## Function Parameters and Arguments:

# a, b, c = "Alakel", "Abdullah", "Khaled"

#print(f"Hello {a}")
#print(f"Hello {b}")
#print(f"Hello {c}")

# def => Function KeyWord [Define]
# say_hello => Function name
# name => Parameter
# print(f"Hello {name}")  => the Task inside Function
# say_hello(a)  => the a when we call the function it's a Argument


# def say_hello(name) :
#     print(f"Hello {name}")


# say_hello(a)    # Alakel
# say_hello(b)    # Abdullah
# say_hello(c)    # Khaled

print("-------------------------------------------------")

# Another Example:

def addition(num1, num2) :
    
    if type(num1) == int and type(num2) == int :

        print(num1 + num2)

    else:

        print("Please Enter Only Integers")

addition("100", "10.3")    # 150
addition(50, 50)     # 100



print("-------------------------------------------------")



# Another Example

def full_name(fName, mName, lName) :     # Parameters
    print(f"{fName.strip().capitalize()} {mName.upper():.1s} {lName.strip().capitalize()}")



full_name("Abdullah  ", "Khaled", "Alakel    ")     # Arguments


print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------


# Function Packing, unpacking Arguments:   *args

# print(1, 2, 3, 4)

# myList = [1, 2, 3, 4, 5, 6, 7]

# print(myList)    # [1, 2, 3, 4, 5, 6, 7]
# print(*myList)    # 1 2 3 4 5 6 7


#def say_hello(name1, name2, name3, name4) :
#    myFriends = [name1, name2, name3, name4]

#   for friend in myFriends :
#        print(f"Hello {friend}")


#say_hello("Alakel","Abdullah","Khaled", "Abdu","Alaa") # here will cause an error because the arguments are 5 and parameters are only 4

# to fix the problem that sometimes we cannot know the exact number of arguments that we gonna use so we can use as per below :

# def say_hello(*names) :      # here you can add the number of arugments when you call the function what ever the number is no problem
#     for name in names:
#         print(f"Hello {name}")



# say_hello("Alakel","Abdullah","Khaled","Sonic","Alnasser")





# Another Example:

def show_detail(*skills) :
    for skill in skills:
        print(f"Hello Alakel You have Skill of: {skill}")



show_detail("HTML","CSS","JS")
# Hello Alakel You have Skill of: HTML
# Hello Alakel You have Skill of: CSS
# Hello Alakel You have Skill of: JS



def show_detail(name, *skills) :
        print(type(skills))      # the type of *skills is Tuple
        print(f"Hello {name} You have these Skills: ")
        for skill in skills :
            print(skill)



show_detail("Abdullah", "HTML","CSS","JS","Python")

# Hello Abdullah You have these Skills:
# HTML
# CSS
# JS

print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------

# Default Parameters (in Function)

def say_hi(name, age = "UnKnown", country = "UnKnown") :
    print(f"Hello {name} Your Age is {age} and You Are From: {country}")


say_hi("Alakel", 25, "Syria")
say_hi("Abdullah", 25, "Germany")
say_hi("Khaled",)   # Error becuase we only put two arguments and its required three arguements for this function
# to fix this issue we put default value for Parameters, you can set the default values for the last parameters or to all

# you can set default values to all parameters without any issue.

print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------


# Function Packing, unpacking arguments:    **KWArgs

def show_skills(**skills) :   #when you put two **, here you say that when you call the function and put arguemnts, it must be Dictionary


    print(type(skills))    # Dictionary

    for skill, value in skills.items() :
        print(f"{skill} => {value}")



show_skills(HTML = "80%", CSS = "50%", JS = "80%")   # you must put here Dictionary Type

myPrivetSkills = {
    "HTML": "80%",
    "Go": "50%",
    "Python": "70%"
}

#show_skills(myPrivetSkills)   # Error You cannot add the dictionary direct here you must first unpack it then you can add it (key:Value)

show_skills(**myPrivetSkills)

print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------

# Advanced Trainings

myTuple = ("HTML", "CSS", "Python")

mySkills = {
    "HTML": "80%",
    "Go": "50%",
    "Python": "70%",
    "SQL": "50%"
}
def show_skills(name, *skills, **skillsWithProgress):
    print(f"Hello {name}: \nSkills Without Progress are:")

    for skill in skills:
        print(f"- {skill}")

    print("Skill With Progress are: ")

    for skillkey, skillvalue in skillsWithProgress.items() :
        print(f"{skillkey} => {skillvalue}")

show_skills("Alakel",*myTuple, **mySkills)



print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------


# Function Scope

# Global Scope
# Local Scope 

# If you want to make a variable inside function global scope as per below:

x = 3

def one():

    global x

    x = 2

    print(x)

print(x)  #3

one()   #2

print(x)    #2

print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------


# Function Recursion:    function call self inside itself

#Example to understand

def cleanWord (word):

    if len(word) == 1 :
        return word

    if word[0] == word[1] :

        print(f"print from condition {word}")
        return cleanWord(word[1:])
    
    print(f"print {word}")
    return word[0] + cleanWord(word[1:])

print(cleanWord("AAAAALLLLLLAAAAAAKKKKKKKEEEEEEELLLLL"))    # ALAKEL


print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------

# Function Lambda  , Anonymous Function

# 1- It has No Name
# 2- You can Call it Inline Without Defining it
# 3- You can use it in return Data From Another Function
# 4- Lambda used For Simple Functions and Def Handle the Larg Tasks
# 5- Lambda is one Single Expression not block of Code
# 6- Lambda type is FUNCTION 

# Normal Function
def say_hello(name, age):

    return f"Hello {name} your age is {age}"


print(say_hello("Alakel", 25))

# Lambda Function

hello = lambda name, age : f"Hello {name} your age is {age}"

print(hello("Abdullah", 26))

# if you want to know the function name, there is a way as per below:

print(say_hello.__name__)    # say_hello
print(hello.__name__)   # Lambda


print(type(hello))   # function



print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------

# File Hanlding:

# "a" Appened     open file for appending values, create file if not exists
# "r" Read        [Default Value] open file for read and give error if files is not exists
# "w" Write       Open File for Writing, Create File if not Exists
# "x" Create      Create File, Give Error if file exists

# import os    # Module os (operating system)

# print(os.getcwd())   # The Main Current Working Directory

# print(os.path.abspath(os.path.dirname(__file__)))   # Directroy For the Opened File


# change Current Working Directory:

# os.chdir(os.path.abspath(os.path.dirname(__file__)))

# print(os.getcwd()) 
# print(os.path.dirname(__file__))

# file = open(r"C:\Users\Abode\Desktop\python\the-summary-of-python\alakel.txt") # the r before " is meaning that it's string don't take programming orders from it

# open method it needs two things ("File Name or File path, the mode that u want") r is default value


########## file reading

# myFile = open(r"C:\Users\Abode\Desktop\python\the-summary-of-python\alakel.txt", "r")

# print(myFile)    # File Data Object  (name, mode, encoding)
# print(myFile.name)   # C:\Users\Abode\Desktop\python\the-summary-of-python\alakel.txt
# print(myFile.mode)    # r
# print(myFile.encoding)  # cp1252


# print(myFile.read())   # read() accept the number of characters that you want to read if not write it, the default value is -1 = read all data
# print(myFile.read(5))   # "Hello" only read 5 characters

# print(myFile.readline()) # Hello Alakel    it will read the line only 
# print(myFile.readline(10))  # How Are Yo

# print(myFile.readlines())  # it return as a list
# print(myFile.readlines(50))  # it return as a list  we put the number of characters that we want
# print(type(myFile.readlines()))   # list


#for line in myFile:

#    print(line)

#    if line.startswith("05"):
#        break

# myFile.close()    # don't forget to close the file after finish the edit on it 


print("-------------------------------------------------")
print("-------------------------------------------------")


# Write and Append in File

# myNewfile = open(r"C:\Users\Abode\Desktop\python\the-summary-of-python\alakel.txt", "w")  ## write mode it will create the file if not exist

# myNewfile.write("Hello From Python File With power\n")
# myNewfile.write("Hello From Python File With love\n")
# myNewfile.write("Hello From Python File With Happy")

# it will remove the old content of the file, then it will write that i mentioned in my previose code it will remove the old content


# myfile = open(r"C:\Users\Abode\Desktop\python\the-summary-of-python\fun.txt","w")
# myfile.write("Alakel Python Summries\n" * 500)



# writelines()    it needs list to work

# myList = ["Alakel\n", "Abode\n", "Abdullah"]

# myFile = open(r"C:\Users\Abode\Desktop\python\the-summary-of-python\abdullah.txt", "w")
# myFile.writelines(myList)


#### Append  the append will not over write on the old file content, it will add on it only without removing it from the file or write on it

# myFile = open(r"C:\Users\Abode\Desktop\python\the-summary-of-python\abdullah.txt", "a")
# myFile.write("\nHello World! \n")
# myFile.write("My Line")

print("-------------------------------------------------")
print("-------------------------------------------------")


# File Handling - Important Info

# myFile = open(r"C:\Users\Abode\Desktop\python\the-summary-of-python\abdullah.txt", "a")  # inside it it has "Hello From Python"

# myFile.truncate(5)   # to cut a chapter from the strings inside the file, truncate() method it needs the number of characters 

# it will return only word "Hello"



#------------------------

# myFile = open(r"C:\Users\Abode\Desktop\python\the-summary-of-python\abdullah.txt", "a") # inside the file we wrote only "Hello"
# print(myFile.tell())  # it will return only 5, this function tell that position of cursor that will start to write if we start to append

# after we make new line by press on enter button and save the line and run the method tell() again it return number 7
# it means that from number 5 jump to number 7 because of the newline,,,, in windows the newline Equal to two characters as \n or \r



#-------------

# myFile = open(r"C:\Users\Abode\Desktop\python\the-summary-of-python\abdullah.txt", "r")# the file content is "Hello From Python With Love"
# myFile.seek(6)     # set the location that you want the cursor start from to count and take

# print(myFile.read())   # it will return "From Python With Love" without Hello 


#--------------

# to remove file from its location

# import os
# os.remove(r"C:\Users\Abode\Desktop\python\the-summary-of-python\abdullah.txt")   # it will remove the file after import the os


print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------


# Built in Functions:

# all()
# any()
# bin()
# id()


# all()  built in function explain as per below example:

x = [1, 2, 3, 4]

if all(x):
    print("All Elements are True")

# here all() is function will check on the list element if all are true if will print "All Elements are True"

else:

    print("There is at least one element false")

print("-------------------------------------------------")
print("-------------------------------------------------")


# any()  built in function explain as per below example:

x = [0, 0, 1, []]

if any(x):

    print("There is one element or more true but minimum one element to write this sentence ")

else:

    print("All the elements are False(No True Elements)")

print("-------------------------------------------------")
print("-------------------------------------------------")

# bin()   built in function, it returns the Binary Code that computer and machine understand it

print(bin(100))   # 0b1100100


print("-------------------------------------------------")
print("-------------------------------------------------")


# id() the id of the variable inside the computer memory that it's unique, it is related to this variable inside the memory cannot be dublicate
# you can know this id thorugh using the built in function id()

a = 1
b = 2

print(id(a))  # 140735829304104
print(id(b))  # 140735829304136



print("-------------------------------------------------")
print("-------------------------------------------------")


# sum(iterable, start)   calculate inside the iterable and give the final result

a = [1, 10, 20, 60]

print(sum(a))   # 91

print(sum(a, 10))   # 101


# round(number, number of digits)    it will make round of the number


print(round(150.299)) # 150
print(round(150.500)) # 150
print(round(150.501)) # 151
print(round(150.551, 2)) # 150.55
print(round(150.555, 2)) # 150.56
print(round(150.554, 2)) # 150.55
print(round(150.554, 3)) # 150.554


# range(start, end, step)    

print(list(range(0)))  # it means the end is 0 the default value of start is 0 and the stop default value is 1
# the result of above is [] because it's start from 0 and end to 0 so it's []

print(list(range(10)))   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] not including the end 
print(list(range(0, 20, 2)))   # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18] not including the end 


# print()

#print("Hello Alakel")
#print("Hello","Alakel")   # default value between two msgs is one space
#print("Alakel","How","Are","You", sep = "|")   # here we change the default seprator between msgs from empty space to |
#print("Alakel","How","Are","You", sep = "@")   # here we change the default seprator between msgs from empty space to @
#print("Alakel","How","Are","You", sep = " @ ")   # here we change the default seprator between msgs from empty space to empty space @ empty space


# whey when we run print function then another print function so the result coming in new line, the answer is because of end.
# the end default value inside the print function is \n it means that new line or start in new line example below to understand:
print("Fist Line", end = "\n")   # end = "\n" default value
print("Second Line", end = "\n")
print("-------------------------------------------------")

print("Third Line", end = " Here The End ")
print("Fourth Line")  # here in this print meaning the end = "\n" so it will start on the new line any print after it
print("Fifth Line")
# output is:
#"Third Line Here The End Fourth Line"
#"Fifth Line"


print("-------------------------------------------------")
print("-------------------------------------------------")


# abs()   absolute value of the number that you gonna give it (absolute value is:  the Distance between your number and 0)

print(abs(1000))  # 1000
print(abs(-1000))  # 1000
print(abs(10.66))  # 10.66
print(abs(-10.66))  # 10.66

print("-------------------------------------------------")


# pow(base, exponent, modulues)    power it's and exponent **

print(pow(2, 10)) # 1024
print(pow(2, 4)) # 16
print(pow(2, 4, 10)) # 6    (2 * 2 * 2 * 2 % 10)
print(pow(2, 5, 10)) # 2    (2 * 2 * 2 * 2 * 2 % 10)


print("-------------------------------------------------")


# min(item,item,item,item) or min(Iterator"Loop")    Minimum() it means to get the minimum element that you have inside the function    

print(min(1, 10, 20, -60, 30, 90))  # -60
print(min("Alakel", "Abdullah","SASA", "FaFA"))   # Abdullah
print(min("A", "L", "M", "Alakel"))   # A
print(min((1, 20, 30, -60, -100, 90)))   # -100

print("-------------------------------------------------")


# max(item,item,item,item) or max(Iterator"Loop")    Maximum() it means to get the maximum element that you have inside the function    

print(max(1, 10, 20, -60, 30, 90))  # 90
print(max("Alakel", "Abdullah","SASA", "FaFA"))   # SASA
print(max("A", "L", "M", "Alakel"))   # M
print(max((1, 20, 30, -60, -100, 90)))   # 90

print("-------------------------------------------------")


# slice(start, end, step)   you can store it inside object and you can use it inside ur application later

# normal without using the slice function:
a = ["A", "B", "C", "D", "E", "F"]
print(a[:])   # ['A', 'B', 'C', 'D', 'E', 'F']
print(a[:5])   # ['A', 'B', 'C', 'D', 'E'] not including the end

# with using slice function 
print(a[slice(5)]) # the number 5 it means that he gonna stop in index number 5    # ['A', 'B', 'C', 'D', 'E']  not including the end
print(a[slice(2, 5)]) # the number 5 it means that he gonna stop in index number 5    # ['C', 'D', 'E']  not including the end


print("-------------------------------------------------")
print("-------------------------------------------------")



# Map  Built In Function (Important)

# 1- Map Take A Fucntion + Iterator
# 2- Make Called Map Becasue it mape the function on every element
# 3- The Function Can Be pre-Defined Function or Lambda Function


# user Map With pre-Defined Function:

def formatName(name):

    return f"- {name.strip().capitalize()} -"

friendsNames = ["  ALakel    ", "Abdullah", "  WaFAa     "]


formatedNames = map(formatName, friendsNames)


# print(formatedNames)   # here it will give the id number of the map object inside the computer memory 

for personName in formatedNames:
    print(personName)
# - Alakel -
# - Abdullah -
# - Wafaa -


print("-------------------------------------------------")
print("-------------------------------------------------")



# Use Map with Lambda Function: 


friendsNames = ["  ALakel    ", "Abdullah", "  WaFAa     "]

formatedNames = map( lambda name : f"- {name.strip().capitalize()} -", friendsNames)

for personName in formatedNames:
    print(personName)


# - Alakel -
# - Abdullah -
# - Wafaa -

print("-------------------------------------------------")
print("-------------------------------------------------")


# Filter()    it always return only the true

# 1- Filter Take A Function + Iterator 
# 2- Filter Run A Function on Every Element
# 3- The Function Can be Pre-Defined Function Or Lambda Function
# 4- Filter Out All Elements For Which the Function Return True
# 5- The Function Need To Return Boolean Value

#Example:

def checkNumbers(num):
    if num > 10 :
        return num
    

myNumbers = [0, 1, 20, 60, 58 , 6,]

myResult = filter(checkNumbers, myNumbers)

# print(myResult) # here it will give the filter object id number inside the computer memory

for n in myResult:
    print(n)

# 20
# 60
# 58

# it return all the numbers is bigger than 10

print("-------------------------------------------------")

# Example to understand the filter that only return the true

def checkNumbers(num):
    if num == 0 :
        return True   # must be put here True to return 0 because filter only return true values and the 0 value is false so must put True
    

myNumbers = [0, 0, 0, 1, 20, 60, 58 , 6, 0, 0]

myResult = filter(checkNumbers, myNumbers)

# print(myResult) # here it will give the filter object id number inside the computer memory

for n in myResult:
    print(n)

# 0
# 0
# 0
# 0
# 0

print("-------------------------------------------------")

# another example to more understand filter() function and how to use it:

def checkNumbers(num):
    return  num > 10  # no need to use condition you can write it direct in return to check the true and filter will return the true elements
    

myNumbers = [0, 1, 20, 60, 58 , 6,]

myResult = filter(checkNumbers, myNumbers)

# print(myResult) # here it will give the filter object id number inside the computer memory

for n in myResult:
    print(n)

# 20
# 60
# 58


print("-------------------------------------------------")


# Another Example For Filter() Function

def checkName(name):

    return name.startswith("A")

myNames = ["Alakel", "Abdullah", "SDOSO", "Wafaa", "Amr"]

myResult = filter(checkName, myNames)

for name in myResult:
    print(name)


# Alakel
# Abdullah
# Amr

print("-------------------------------------------------")

# Example using filter Function For Lambda Function:

myNames = ["Alakel", "Abdullah", "SDOSO", "Wafaa", "Amr", "Wael"]

myResult = filter(lambda name : name.startswith("W"), myNames)

for n in myResult:
    print(n)

#Wafaa
#Wael

print("-------------------------------------------------")
print("-------------------------------------------------")





# reduce()   higher order Function so it will transfer to function tool Module

# 1- Reduce Take A function + iterator
# 2- Reduce Run A function on First and Second Element and give Result
# 3- Then Run Function On Result and third Element
# 4- Then Run Function on Result and Fourth Element and So On......
# 5- Till one element is left and this is the result of the reduce
# 6- The Function Can be pre-Defined Function Or Lambda Function

# Example: 

from functools import reduce

def sumAll(num1, num2):

    return num1 + num2


numbers = [1, 6, 8, 100, 33]

result = reduce(sumAll, numbers)

print(result)   # 148   ((((1 + 6) + 8 ) + 100)+ 33)  = 148



# Lambda Function With Reduce():

from functools import reduce

numbers = [1, 6, 8, 100, 33]

result = reduce(lambda n1, n2 : n1 + n2, numbers)

print(result)   # 148    ((((1 + 6) + 8 ) + 100)+ 33)  = 148


print("-------------------------------------------------")
print("-------------------------------------------------")

# below we have three built in functions:
# enumerate()
# help()
# reversed()

print("-------------------------------------------------")
print("-------------------------------------------------")

# enumerate(iterable, start = 0)   it will add counter to the iterable when you are in the loop

# Example:

mySkills = ["HTML", "CSS", "Java", "PHP"]

mySkillsWithCounter = enumerate(mySkills, 10)


for c, s in mySkillsWithCounter :   # because of enumerate function you can loop on two element one is the counter and one is skill
    print(f"{c} - {s}")

# 10 - HTML
# 11 - CSS
# 12 - Java
# 13 - PHP

# if you want to check the type of data mySkillsWithCounter:
#print(type(mySkillsWithCounter))    # <class 'enumerate'>



print("-------------------------------------------------")
print("-------------------------------------------------")

# help() if you want to know details about any function  

#print(help(print))


print("-------------------------------------------------")
print("-------------------------------------------------")

# reversed()   it will reverse the iterable 

myString = "Alakel"

print(reversed(myString))   # <reversed object at 0x000001496D4DF9A0>

for letter in reversed(myString):   # you want to loop on it to see the reverse on the iterable
    print(letter)
# l
# e
# k
# a
# l
# A

for skill in reversed(mySkills):
    print(skill)

# PHP
# Java
# CSS
# HTML

# you can make it list then you can loop on it with add list() and you can store it inside variable to use it later in app

print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------



######### Modules => Build in Modules

# 1- Module is a File Contains a set of Functions 
# 2- You can Import Module in your App to Help You
# 3- You Can import Multiple Modules
# 4- You Can Create Your own Modules
# 5- Modules Saves Your Time


# Import Main Module

# import random    # here you import the full module with all the functions inside it

# print(random) after import you can print it to know the location of the module on your computer
# print(f"Print Randome Float Number {random.random()}") # it will generate random float number


# show all functions inside module:
# print(dir(random)) # here to know all the functions inside the module


# import one or two functions from module, you don't want to import the full module:

# from random import randint , random # made import for two functions(randint, random) from the random module
# print(f"Print Random Integer: {randint(100, 500)}")  # here it will generate number between 100 and 500 integer number
# print(f"Print Float random number: {random()}")   # here it will generate random float number


print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------

# Modules => Create Your Module 

# You Must Create Your Module Example Here, I Create my Module with file name alakel.py

# You may need to import sys Module because: it will give the paths system for python and 
# search for the module that you want to make import for it even if you want to import a specific module in the run time too
# import sys
# sys.path.append(r"D:\project")  # here if you want to add path in the run time and this path that has your module that you want to add
# print(sys.path)

# import alakel   # import my module

# # print(dir(alakel))   # here you can see the functions inside your module 

# alakel.sayHello("Abdullah")
# alakel.sayHello("Sarah")

# alakel.sayHowAreU("Maya")
# alakel.sayHowAreU("Layan")


print("-------------------------------------------------")
print("-------------------------------------------------")


# import alakel as aa   # import my module as aa: as aa mean you want to give a short name or nickname or alias to your module to use it


# aa.sayHello("Abdullah")
# aa.sayHello("Sarah")

# aa.sayHowAreU("Maya")
# aa.sayHowAreU("Layan")


print("-------------------------------------------------")
print("-------------------------------------------------")

# from alakel import sayHello  ## here we import only one function from our module 
# sayHello("Abdullah")

print("-------------------------------------------------")
print("-------------------------------------------------")

# from alakel import sayHowAreU as hru   # here we import one function from module and we give it a alias name (nickname)
# # hru("Abode")


print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------

### Modules => Install External Packages

# 1- Module VS Package
# Module: Single file has functions to work with in your project
# Package: is multiple modules and files related to this package

# 2- External Packages Downloaded From The Internet.
# 3- You Can Install Packages with Python Package Manager PIP
# 4- PIP install the package and its dependencies(another packages or things that based and related to that package that you want to install)
# 5- Modules List "https://docs.python.org/3/py-modindex.html"  (Modules Built in with python language if you want to read documantation)
# 6- Packages and Modules Directory "https://pypi.org/"  (for the External Packages to search and take what you want)
# 7- PIP Manual "https://pip.pypa.io/en/stable/cli/pip_install/"

##### you must install pip python package manager

## inside terminal you can write below:
# to know which pip version you have in you system:  pip --version
# to know all the packages that you already have:    pip list
# to install specific package through:     pip install packageName example:   pip install termcolor
# also you can write module name:  pip install module name  or  pip install pyfiglet >= 1.0.4  (Here to install this version or more new)
# to upgrade any package or module that you have or even the pip:   pip install pip --upgrade  if error: pip install --user pip --upgrade


import termcolor    # import the termcolor
import pyfiglet     # import the pyfiglet

print(dir(pyfiglet))  # to know all the function inside the pyfiglet package

print(pyfiglet.figlet_format("Alakel"))    # with asci art
print(pyfiglet.figlet_format("Abode"))      # with asci art 

print(termcolor.colored("Alakel", color="blue"))   # change the color of the word

print(termcolor.colored(pyfiglet.figlet_format("Alakel"), color="blue"))  # used asci art with color changed




print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------


## Date and Time => Introduction

# date and time it's a module inside python

import datetime

#print(dir(datetime))  to know all the info inside datetime module
#print(dir(datetime.datetime)) to know the method inside datetime method name = datetime

# print the current date and time:

print(datetime.datetime.now())   # 2023-07-26 23:44:17.936864     the exact time and date

print(datetime.datetime.now().year)   # 2023
print(datetime.datetime.now().month)   #  7
print(datetime.datetime.now().day)    # 26


# print start and end of date:
print(datetime.datetime.min)   # 0001-01-01 00:00:00
print(datetime.datetime.max)   # 9999-12-31 23:59:59.999999


# print(dir(datetime.datetime.now())) ## to know all inside of now(), one of the important inside it is time()

# print the current time:


print(datetime.datetime.now().time())   #23:48:35.038357
# the current time each one:
print(datetime.datetime.now().time().hour)   # 23    hour
print(datetime.datetime.now().time().minute)   # 49   minutes
print(datetime.datetime.now().time().second)    # 6    seconds 

print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------

# print start and end of time:

print(datetime.time.min)   # 00:00:00
print(datetime.time.max)   # 23:59:59.999999

print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------


# if i want to print specific date:

print(datetime.datetime(1995, 6, 21))    # 1995-06-21 00:00:00    but the year, month, day are required to proceed with function and time optional
print(datetime.datetime(1995, 6 ,21, 10, 45, 55, 155))   # 1995-06-21 10:45:55.000155

print("-------------------------------------------------")
print("-------------------------------------------------")

# Small Example to collect how many days that i lived:

birthDay = datetime.datetime(1995, 6, 21)
dateNow = datetime.datetime.now()


print(f"My Birthday is {birthDay} and", end=" ")
print(f"Date Now Is {dateNow}")


print(f"I Lived For {(dateNow - birthDay).days} Days.")   # to return only the days how many days i lived till now

print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------


#### how to make format for date and time:

import datetime

myBirthday = datetime.datetime(1995, 6, 21)

print(myBirthday)  # 1995-06-21 00:00:00


print(myBirthday.strftime("%B"))  # June
print(myBirthday.strftime("%b"))   # Jun
print(myBirthday.strftime("%a"))    # Wed
print(myBirthday.strftime("%A"))    # Wednesday

# to know the strftime directive you must visit https://strftime.org/  to know what you want to print exactly the day, month or even what you want

print(myBirthday.strftime("%d, %B, %Y"))   # 21, June, 1995
print(myBirthday.strftime("%d-%B-%Y"))   # 21-June-1995


print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------

# back to scope section local and global:

# the nonlocal keyword:


# example: in the below example we have issue that the local variable 'my_age' referenced before assignment!!!!!!

# def which_scope():
#     my_age = 49 # local variable my_age
#     def inner_scope():
#         my_age += 1 # Issue when we try to run this line.
#         print(my_age)
#     inner_scope()

# which_scope()


# to fix this issue we use keyword nonlocal:

def which_scope():
    my_age = 49 # local variable my_age
    def inner_scope():
        nonlocal my_age # No longer an issue because of this
        my_age += 1
        print(my_age)
    inner_scope()

which_scope()    # 50


print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------

## Iterable VS Iterator:

# Iterable:
# 1- Object Contains Data that can be Interated on
# 2- Example(String, List, Tuple, Dictionary)

# Examples
myString = "alakel"

for letter in myString:
    print(letter, end=" ")

print("\n########")
myList = [1, 2, 3, 4, 8, 10 , 9]

for n in myList:
    print(n, end =" ")



#myNumber = 10
#myNumber = 10.10
#myNumber = False

#for n in myNumber:
#    print(n)     # Error Int Is not Iterable , Float also not , boolean Not Also

print("-------------------------------------------------")

# Iterator:

# 1- Object Used To Iterate over iterable using next() Method Return 1 Element at A Time
# 2- You can generate iterator from the iterable when we are using iter() method
# 3- For loop already Calls iter() method on the iterable behind the scene
# 4- Gives "StopIteration" if there is not next element


#Example:

myString = "Alakel"

#print(next(myString))  #Error here, it will show that str object is not an iterator

myIterator = iter(myString)   # to convert to iterator the you can use next method on it

# next method needs iterator not an Object
#print(next(myIterator)) #A     
#print(next(myIterator)) #l
#print(next(myIterator)) #a
#print(next(myIterator)) #k
#print(next(myIterator)) #e
#print(next(myIterator)) #l
#print(next(myIterator)) # StopIteration    for loop when it reach to this line it will break the loop auto


for myWord in "Abdullah":    # for in the behind the scene make :     iter("Abdullah")  then used the next() method till each stop iteration
    print(myWord, end=" ")                                                             # then it will break the loop

print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------


## Generators :

# 1- Generator is a function with "yield" keyword instead of "return"
# 2- It's Support iteration and return Generator iterator by calling "yield"
# 3- Generator function can have one or more "yield"
# 4- By using next() it resume from where it called "yield" Not from the begining
# 5- when called, it's not start auto, it is only give you the control

def myGenerator():

    yield 1
    yield 2
    yield 3
    yield 4


print(type(myGenerator()))  # 'generator'
print(myGenerator())  # <generator object myGenerator at 0x00000207508F5430>

myGenerator()   # not result will shown becuase it's not behaviour same normal function

# myGen = myGenerator()

# print(next(myGen))  # 1
# print("Hey")
# print(next(myGen))  # 2
# print("How")
# print(next(myGen))  # 3
# print("SOSO")
# print(next(myGen))  # 4


for num in myGenerator():

    print(num)



print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------


# Decorators => Intro     in other programming languages its called meta programming 

# 1- SomeTimes Called Meta Programming
# 2- everthing in python is object even the functions 
# 3- Decorator take a function and add some functionality and return it
# 4- Decorator wrap other function and enhance their behaviour 
# 5- Decorator is Higher Order Function (Function Accept Function As Parameter)


def myDecorator(func):   # Decorator(function as parameter)

    def netsedFunc():    # anyname you can set (this function wrap all the decoration inside this function)
    
        print("before")   # message from decorator

        func()     # execute the function

        print("after")   # message from decorator

    return netsedFunc    # here will return all data after set the decoration too


@myDecorator
def sayHello():

    print("Hello From SayHello Function")


sayHello()

print("-------------------------------------------------")

@myDecorator
def sayhowareU():
    print("Hello From sayhowareU Function")


sayhowareU()



print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------



# Decorators => Function With Parameters




def myDecorator(func):   # Decorator(function as parameter)

    def netsedFunc(num1, num2):    # anyname you can set (this function wrap all the decoration inside this function)
    
        if num1 < 0 or num1 < 0:

            print("One or Two Of the Numbers is less than 0")

        func(num1, num2)     # execute the function


    return netsedFunc    # here will return all data after set the decoration too


def myDecoratorTwo(func):

    def nestedFun(num1, num2):

        print("I'm Decorator Two")

        func(num1, num2)


    return nestedFun



@myDecorator
@myDecoratorTwo
def calculate (n1, n2):
    print(n1 + n2)



calculate(10,20)

calculate(5,20)   

# the reason of using decorators because its increase the functionality of your function as per previous example: inside the decorator 
# check if the number 1 or number 2 are less than 0 so it will show a message, so it add more factionality 

# we can use more than one decorator before/in one function




print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------


#Decorators Speed Test (Advanced Practical)


def myDecorator(func):   

    def netsedFunc(*numbers):    
    
        for num in numbers:

            if num < 0:

                print("One or Two Of the Numbers is less than 0")


        func(*numbers)     


    return netsedFunc   



@myDecorator
def calculators(n1, n2, n3, n4, n5):

    print(n1 + n2 + n3 + n4 + n5)


calculators(20, 90, 400, 582, -2)

# the example above it will accepts un limited of arguments that decorator using *numbers so no limited for the numbers we can change as we want





# speed test example:
# from time import time

# def speedTest(func):

#     def wrapper():

#         start = time()    # time is floating point number

#         func()

#         end = time()


#         print(f"Function Running Time Is: {end - start}")


#     return wrapper



# @speedTest      # Function Running Time Is: 2.359846353530884 the result not fixed is to check the second till the function is finished
# def bigMac():
#     for number in range(1, 20000):

#         print(number)

# bigMac()


print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------


## loop on many with zip()  : it is built in function that give you ability to loop on more iterable object

# zip() return a zip object contains all objects
# zip() length is the length of the lowest object that made iterable on it


# list1 = [1, 2, 3, 4, 5]
# list2 = ["A", "B"]


# ultimateList = zip(list1, list2)

# print(ultimateList)    # <zip object at 0x000002282FD67B80>

# for item in ultimateList:
#     print(item)


# (1, 'A')
# (2, 'B')
# the output as per above why? because as i mentioed the lowest object will control the zip() function length

print("-------------------------------------------------")

list1 = [1, 2, 3, 4, 5]
list2 = ["A", "B", "C", "D"]
tuple1 = ("Man", "Woman", "Girl", "Boy")
dict1 = {"Name": "Alakel", "Age": 25, "Country": "Syria"}



for item1, item2, item3, item4 in zip(list1, list2, tuple1, dict1):
    print("List 1 item =>", item1)
    print("List 2 item =>", item2)
    print("Tuple 1 item =>", item3)
    print("Dict 1 item =>", item4, "Value =>", dict1[item4])



# Out Put the reason that it shows three results only becasue of the length of dictionary(Dict1) only three elements so it will follow it 
# List 1 item => 1
# List 2 item => A
# Tuple 1 item => Man
# Dict 1 item => Name Value => Alakel
# List 1 item => 2
# List 2 item => B
# Tuple 1 item => Woman
# Dict 1 item => Age Value => 25
# List 1 item => 3
# List 2 item => C
# Tuple 1 item => Girl
# Dict 1 item => Country Value => Syria


print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------

## Practical => Image Manipulation with Pillow:

# # how to install pillow library:

# # open terminal: write:  pip install pillow



# from PIL import Image

# myImage = Image.open("assets/images/img1.jpg")


# # show the image :
# myImage.show()

# # Edit the image and crop it

# myCropImage = (100, 100, 800, 800)     # here the box crop diminsion needs (Left, Upper, Right, Lower)

# myNewImage = myImage.crop(myCropImage)

# # show the new image:
# myNewImage.show()



# # the library/package pillow if you want to make edit on images: Crop, black and white, change type of the image from type to type, roll
# # put two or more images in one photo , change contrast of the image 


# # the Convert Image:

# myConvertImage = myImage.convert("L")

# myConvertImage.show()    # here the photo changed to gray scale image Important 

# # you can visit to see what you can do with this package, it is really amazing package for photos: https://pillow.readthedocs.io/en/stable/



# # Picture Manipulation: Pillow Package.


print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------

## Doc String and Commenting and Documenting:

# 1- Documentation String for Class, Module or Function
# 2- Can be Accessed from the help and Doc Attributes
# 3- Made for Understanding the Complex Code
# 4- There is one line and multiple line doc Strings


# def alakel_function(name):
#     ''' This Is Function To Say Hello From Alakel Function '''   # this is document for the function (Single Line Doc String)

#     """ 
#     Alakel Function
#     It Say Hello From Inside the Function
#     The Parameter: name => for the person that show his Fname

#     return: Hello (person name) from alakel function

#     """
#     print(f"Hello {name} From Alakel Function")


# alakel_function("Abdullah")


# #print(dir(alakel_function))  # here to see all the attributes and info inside the function -  we use dir()

# # print(alakel_function.__doc__)  ### here you can see what you write inside the doc ''' '''  single line doc
#                                    ## Here You Can see Also for the Multiple line Doc """ """ multiple line doc

# help(alakel_function)   ## Here YOu Can see what you write inside the doc ''' ''' single line doc
#                         ## Here You Can see Also for the Multiple line Doc """ """ multiple line doc

print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------

## Installing and Use pylint for better code: it will guide you to write clean, right , best practise, right name convenstion, style of code
# it will guide you to follow the standards of write code
## to install pyline: open terminal write : pip install pylint



# to check the rate for your file that if follows the standard or not and what is the rate that you got, you gonna write inside terminal:

# pylint.exe then the python file path example:

# pylint.exe C:\Users\Abode\Desktop\python\the-summary-of-python\first.py   (write it inside the terminal)  Your code has been rated at 4.16/10


print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------


# Errors and Exceptions Raising:

# 1- Exceptions is a Runtime Error Reporting Machanism
# 2- Exceptions Gives You the Message to understand The problem
# 3- Traceback Gives You the Line To look for the code in this line
# 4- Exceptions have many types such as: (Syntax Error, Index Error, Key Error, Etc....) https://docs.python.org/3/library/exceptions.html
# 5- Raise Keyword used to Raise Your Own Exceptions (Very Important Thinking)

# Example for make and raise Your own Exceptions:
# Very Important to make you own Exceptions inside you application to know the problem

#Example:

# x = -10

# if x < 0:
    
#     raise Exception("The Number Is less than 0")   #here it will stop all the code and show it in the terminal as mentioned inside exception
#                                                    # Also here it will show traceback and show the exact line that issue happened in it
#     print("This Will not print because of the Error")
# else:

#     print("x Is Positive Number")



# print("This Message After If Condition")



#Example:

# a = "Alakel"

# if type(a) != int:
    
#     raise ValueError("Only Numbers Allowed")  # showed traceback and the exact line of the issue



# print("Print Message After Condition")  # if a is a number it will run normal and there is no value error or even exception to show and stop


print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------


## Exceptions Handling:

# Try | Except | Else | Finally

#Try => Test The Code For Errors
#Except => Handle The Errors

#Else => If No Errors 
#Finally => Run The Code

# number = int(input("Write Your Age: "))   # if the user write string (word) not integer it will return Value Error

# print(number)

# print(type(number))

## try cannot work without except, so it's together
# try: ### Here You Try The Code And Test The Errors

#     number = int(input("Write Your Age: "))

#     print("This Is Integer, from Try")

# except:  ### Here It will handle And Show the Error, if it's found

#     print("The User Input Not Integer")


# else:   # if There is No Error, it will proceed with the code, you can also write inside try if you don't want to use else

#     print("This Is Integer, from Else")   

# finally:   ## it will proceed what ever the situation 

#     print("print from finally what ever the result")



# Another Example Below to Understand the logic of these words:

# print(10/0)    ## Error Zero Division Error

# try:

#     print(10/0)
#     print(x)

# except:

#     print("Cannot Divide")

# the Issue Above what ever the error it will show cannot divide !!


# again the Example with more detials
# try:

#     # print(10/0)
#     # print(q)
#     print(int("Hello"))

# except ZeroDivisionError:    ## in the except we put the exact error that we want to show the msg below when it happened

#     print("Cannot Divide")

# except NameError:

#     print("The Variable Not Found")


# except ValueError:

#     print("You Put Value Error")

# # except:    ## here if you want to catch errors that not mentioed in the previous excepts so it will catch the other errors when they happened

# #     print("General Error Happened")

print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------


## Exceptions Handling:
### Advanced Example: we make the number of tries that wrote the file name to open it, it will reduce the count if it'S wrong name

# the_file = None

# the_tries = 5

# while the_tries > 0:

#     try:    # try to open the file
#         print("Enter The File Name Absolute Path to Open")

#         print(f"{the_tries} Tries left!")

#         print(r"Example: C:\Users\Abode\Desktop\python\the-summary-of-python\yourFile.Extension")


#         file_name_and_path = input("File Name => : ").strip()


#         the_file = open(file_name_and_path, "r")

#         print(the_file.read())

#         break

#     except FileNotFoundError: ## if there is an error

#         print("The File Not Found Please Enter the Valid Name")
#         the_tries -= 1

#     except:

#         print("Error!")



#     finally:     #here anyway will proceed and run even if the file not run in try operation so we put condition in the finally:

#         if the_file is not None:

#             the_file.close()

#             print("File Closed")

# else:

#     print("Sorry! All Your Tries Finished")

print("-------------------------------------------------")
print("-------------------------------------------------")
#------------------------------------------------------------------------------------------------------------

## Debugging Code:   using breakpoint and allow it in VS-code then press run and debug then you can follow your code step by step 
## to follow what heppened in each step with using breakpoints


## very important stop(debugging) in complex apps to know the errors and trace it



#------------------------------------------------------------------------------------------------------------


## Type Hinting: it is only a hint and it's also different from the code documentation that we mention in previous section
# and type of data   examples:   -> int   -> float  -> str    -> list ......



def say_hello(name) -> str:     ## -> str      it's a hint but the user can enter another value but here i only hint for the developer 
    print(f"Hello {name}")          ## what the parameter data type gonna accept  



say_hello("Alakel")


def calc(num1, num2) -> int :   ## -> int    it's a hint but user can enter any other value  (it's only hint)


    print(num1 + num2)



calc(10, 10)


#------------------------------------------------------------------------------------------------------------
print("-------------------------------------------------")
print("-------------------------------------------------")



# Regular Expressions:  Intro  (Please use The websites below very important to check the regular expression and know all)

# 1- Squesnce Of Characters That Define A search Pattern
# 2- Regular Experssion is Not in Python It is General Concept
# 3- Used in [Credit Card Validation, IP Address Validation, Email Validation]
# 4- Test RegEx "https://pythex.org"
# 5- Characters Sheet: "https://www.debuggex.com/cheatsheet/regex/python"

# Regular Expressions => Quantifiers   specail character that related to quantity 


# Characters Sheet => Regular Expression Quantifiers "https://www.debuggex.com/cheatsheet/regex/python"



#Example

#011 5456-80
#011 5456-33
#011 3434-44
#Hello
#My Name Is Alakel
#123456798

# i want to select the phone number

#\d{3}\s\d{4}-\d{3}


# very very very important Website for regular Expression:  https://regex101.com  it will describe the regular expression that u want to use it
# so it's very important website to use it


#-------------------------------------------------------

# Regular Expressions => Characters Classes Trainings:


# Characters Sheet => Characters Classes "https://www.debuggex.com/cheatsheet/regex/python"

# [abd]  it will search  for each letter inside these brackets so it'S important
# [a-z] from a to z
# [0-9] from 0 to 9
# [a-z0-9] from a to z and from 0 to 9
# [a-zA-Z0-9]
# [a-m]
# [^N] it will bring all except N
# [^a-z] it wll bring all except from a to z small
# [^a-z0-9] it will bring all except from a to z small and also from 0 to 9

# \s[0-9]   it means bring space then number between 0 and 9
# _[0-9] it means bring _ then number between 0 tp 9
#_[A-Z] it means bring _ then letter between A to Z 
#_[a-z] it means bring _ then letter between a to z


#Example: \s[A-Z]{2}\s[0-9]{3}\s\w{,6}

# Important to understand ? inside Regular Expression Quantifiers

# \d{3}\s\d{4}-?\s?\d{3}     below the five lines it will bring all with this regular expression

# => 012 1234 567
# => 012 1234-567
# 012 1234 567
# 012 1234-567
# 012 1234- 567
#-------------------------------------------------------

### Regular Expressions: => Assertions

# ^ Start Of String
# $ End Of String


# ^\d{3}\s\d{4}-?\s?\d{3} 

# it will bring below becasuse it starts with and no problem for what ends with
# 012 1234 567=>
# 012 1234-567=>




# \d{3}\s\d{4}-?\s?\d{3}$

# it will bring below becasue it ends with and no problem with what starts with:
# =>012 1234 567
# =>012 1234-567




# ^\d{3}\s\d{4}-?\s?\d{3}$

# it will bring below becuase it ends and starts with:
# 012 1234 567
# 012 1234-567



#####
# Note: # [A-z] it means [A-Za-z]
# make Email with regular expressions

#[A-z0-9\.]+@[A-z0-9]+\.[A-z]+

#abdullah@gmail.com
#aslsdada1122@gmail.org
#dsfdsfafd_alll@hotmail.ae
#dsfdsfafd_alll@hotmail.de


#[A-z0-9\.]+@[A-z0-9]+\.(com|net|org)
#abdullah@gmail.com
#aslsdada1122@gmail.org


# "https://regex101.com"    please use it to understand the regular expressions



#-------------------------------------------------------

# Regular Expresssion => Logical Or And Escaping

# | or
# \ Escape Special Characters
# () Separate Groups
# ----------------------------


#Example to Understand:

# (\d-|\d\)|\d>) (\w+)

# 1- HTML
# 2- CSS
# 3- Python

# 1) HTML
# 2) CSS
# 3) Python

# 1> HTML
# 2> CSS
# 3> Python

# ----------------------------


# another Example:

# (\d{3}) (\d{4}) (\d{3}|\(\d{3}\))


# 012 4578 256
# 012 4578 213
# 011 4569 (222)
# 011 4569 (789)

# ----------------------------


# another Example:

# (https?://)(www\.)?(\w+)\.(net|org|com)

# http://www.alakel.net
# http://alakel.org
# http://abdullahalakel.com



# check the above examples on website : "https://pythex.org"   important to see the exact result


#-------------------------------------------------------------


# Regular Expressions => Re Module Search and FindAll

# search() => Search A String for A match and return A First Match Only....please be note that it returns only the first match not all 
# findall() => Returns A List of All Matches and Empty List if No Match

# Email Pattern => [A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)


# to use regular expression inside Python you must import the module re

# import re

# my_string = re.search(r"[A-Z]", "abdullah Alakel")

# print(my_string)    # <re.Match object; span=(9, 10), match='A'>
# print(dir(my_string))   # you gonna see all the info about the method and see the other methods inside it

# print(my_string.span())   # (9, 10)
# print(my_string.string)   # abdullah Alakel

# print(my_string.group())   # A

# print("-------------------------------------------------")
# print("-------------------------------------------------")
# # another Example:

# my_search = re.search(r"[A-Z]{2}", "ABdullahAlakel")
# print(my_search.span())  # (0, 2)
# print(my_search.string)   # ABdullahAlakel
# print(my_search.group())    # AB

# print("-------------------------------------------------")
# print("-------------------------------------------------")

# # Advanced Example that show it's a valid Email or Not Valid Email, Important Example to understand

# is_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)", "alakel@alakel@.com")  # Sorry!, It's Not A valid Email

# is_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)", "alakel@alakel.com") # It's a Valid Email, Thank You

# if is_email:

#     print("It's a Valid Email, Thank You")

#     print(is_email.span())
#     print(is_email.string)
#     print(is_email.group())
# else:

#     print("Sorry!, It's Not A valid Email")


# print("-------------------------------------------------")
# print("-------------------------------------------------")


# email_input = input("Please Write YOur Emial: ")

# search = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.com|net|org|info", email_input)

# empty_list = []

# if search != []:
    
#     empty_list.append(search)

#     print("Email Added")


# else:
#     print("Invalid Email !!")


# for mail in empty_list:
#     print(mail)

# important note: to return the full email without groups and captures you must remove () to don't make groups becauase if you put
# the last (com|net|org|info) as group the mail will return the only this so becarful about it



print("-------------------------------------------------")
print("-------------------------------------------------")

#-------------------------------------------------------------

# ## Regular Expressions => re Module And Sub

# # split(pattern, string, Maxsplit) => return a list elements splitted on each match
# # sub(pattern , string, replaceCount) => replace matches with what you want 


# import re

# # Split cut the string and cut it as per the match
# string_one = "I Love Python and JavaScipt"

# search_one = re.split(r"\s", string_one)   # \s means that in each space found in my string

# print(search_one)    ## ["I", "Love", "Python"]


# search_two = re.split(r"\s", string_one, 1)   # here we specify that we want only one time split then put the rest together

# print(search_two) # ['I', 'Love Python and JavaScipt']

# #----------------------------------------------------------------
# print("-------------------------------------------------")
# print("-------------------------------------------------")

# string_two = "How-To_Write_A_Very-Good-Article"

# search_three = re.split(r"_", string_two)

# print(search_three)   # ['How-To', 'Write', 'A', 'Very-Good-Article']

# search_four = re.split(r"_|-", string_two)

# print(search_four)  # ['How', 'To', 'Write', 'A', 'Very', 'Good', 'Article']

# print("-------------------------------------------------")

# # Get Words From URL:

# for counter, word in enumerate(search_four, 1):
#     if len(word) == 1: # we put the condition here to escape the a from the result because it is only one letter so no need to see on result

#         continue

#     print(f"Word Number: {counter} => {word.lower()}")



#output for above example is :
# Word Number: 1 => how
# Word Number: 2 => to
# Word Number: 3 => write
# Word Number: 5 => very
# Word Number: 6 => good
# Word Number: 7 => article    
print("-------------------------------------------------")


# string_one = "I Love Python and JavaScipt"

# print(re.sub(r"\s", "-", string_one))   # I-Love-Python-and-JavaScipt


# print(re.sub(r"\s", "-", string_one, 1))  # I-Love Python and JavaScipt

print("-------------------------------------------------")
#-------------------------------------------------------------
print("-------------------------------------------------")

# Regular Expressions => Group Trainings and Flags:

import re

#(https?) it will take the http and https

#(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)     # this regular expression will match all below:

#1- https://www.alakel.org:8080/catergory.php?article=105?name=how-to-do
#2- https://www.alakel.org:category.php?article=105?name=how-to-do
#3- https://alakel.org/category=50?article=105?name=how-to-do
#4- http://alakel.org/category=50?article=105?name=-hpw-to-do
#5- http://alakel.org
#6- http://alakel.net


# my_site = "https://www.alakel.org:8080/catergory.php?article=105?name=how-to-do"

# search = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", my_site)

# print(dir(search))   # will show all methods inside it: focus on group and groups methods


# print(search.group())   # https://www.alakel.org:8080/catergory.php?article=105?name=how-to-do
# print(search.groups())   # ('https', 'www', 'alakel', 'org', '8080', 'catergory.php?article=105?name=how-to-do')

# for group in search.groups():
#     print(group)

# output loop
#  https
#  www
#  alakel
#  org
#  8080
#  catergory.php?article=105?name=how-to-do


# print(f"protocol: {search.group(1)}")   # protocol: https
# print(f"Sub Domain: {search.group(2)}")    # Sub Domain: www
# print(f"Domain Name: {search.group(3)}")   # Domain Name: alakel
# print(f"Top Level Domain: {search.group(4)}")   # Top Level Domain: org
# print(f"Port: {search.group(5)}")    # Port: 8080
# print(f"Query String: {search.group(6)}")   # Query String: catergory.php?article=105?name=how-to-do



#### Important Note: Please Focus On "https://pythex.org" website very important
# Inside this website there is Button name: IGNORECASE : so you can write and match without letter case sensitive
# Inside this website there is button name: VERBOS: so You can write comment #comment so it will ignore the comments inside the regular expression
# please be note (.) that it's match all characters except newline (\n) but with button DOTALL will match everthing with newline too
# Multiline Button inside the website: if you write more than one line you must press multiline


# when you want to use the above info from website inside the python language as per below:

# search = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", my_site, re.M)   #MultiLine
# search = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", my_site, re.I)   #Ignore Case
# search = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", my_site, re.DOTALL)   #DOTALL 


print("-------------------------------------------------")
#-------------------------------------------------------------
print("-------------------------------------------------")

print("-------------------------------------------------")
#-------------------------------------------------------------
print("-------------------------------------------------")

# Object Oriented Programming: OOP Intro
# 1- Python Support Object Oriented Programming
# 2- OOP Is A Paradigm or Coding Style
# 3- Paradigm => Means Structuring Program So the Methods[Functions] and Attributes[Data] are Bundled into Object
# 4- Methods => Act as Function that use the information of the object
# 5- Python Is Multi-Paradigm Programming Language [Procedural, OOP, Functional]
# 6- Procedural => Structure App Like Recipe, Sets of steps to make the task
# 7- Functional => Built on the Concept of Mathematical Functions 


# Why OOP ?

# OOP Allow you to Organize your code and make it readable and reusable(More Than one time use it)
# Everything in Python is Object

# If Man Is Object:
# Attributes => Name, Age, Address, Phone Number, Info              * In JavaScript its name is (Properties = Attributes)
# Methods [Behaviors] => Walking, Eating, Playing, Typing, Sleeping

# If Cas IS Object:
# Attributes => Model, Color, Price,
# Methods => the cas is Stopping, the cas is going 


# Class:
# 1- Class Is The Template For Creating Objects [Object Constructor | Blueprint]
# 2- Class Car Can Create Many Cars Object
# 3- Class User Can Create Many Users Object

#-------------------------------------------------------------

## OOP : Class Syntax and Info

# 1- Class is the Blueprint or Constructor of the Object
# 2- Class Instantiate means Create Instance Of A Class
# 3- Instance => Object Created from Class and have Their Methods and Attributes 
# 4- Class Defined with keyword Class
# 5- Class Name Written with PascalCase [UpperCamelCase] Style
# 6- Class May or May not Contains Methods and Attributes 
# 7- When Creating Object Python look for the built in __init__ method
# 8- __init__ method called every time you create object from class
# 9- __init__ method is initialize the Data for the object
# 10- Any method with two underscore in the start and end called Dunder or Magic Method
# 11- Self Refer to the current Instance Created from the class and must be the first Parameter
# 12- Self Parameter Can be Named Anything if you want not only self
# 13- In Python You Don't need to call new() keyword to create object


# Syntax:
# class Name:
#     Constructor => Do Instantiation [ Create Instance From A class ]
#     Each Instance Is Separate Object
#     def __init__(self, other_data)
#         Body Of Function


# Simple Example:

# class Member:

#     def __init__(self) :

#         print("A New Member Has Been Added")


# Member()
# Member()
# Member()

# member_one = Member()
# member_two = Member()
# member_three = Member()


# print(member_one.__class__) # class name (Member) , it will show us from which class come or reffer to

#-------------------------------------------------------------

# OOP => Instance Attributes and Methods:

# Self: Point & reffer To Instance Created From Class
# Instance Attributes: Instance Attributes Defined Inside the Constructor

# Important Instance Methods: Take Self Parameter Which point To Instance Created From Class
# Instance Methods: Can Have More Than One Parameter Like Any Function
# Instance Methods: Can Freely Access Attributes and Methods On The Same Object
# Instance Methods: Can Access The Class Itself


# class Member:

#     def __init__(self, first_name, middle_name, last_name, gender) :    # Important Note: Instance Attributes will be Inside Constructor

#         self.fname = first_name
#         self.mname = middle_name
#         self.lname = last_name
#         self.gender = gender


#     def get_full_name(self) :

#         return f"{self.fname} {self.mname} {self.lname}"


#     def name_with_title(self) :

#         if self.gender == "Male":
#             return f"Hello Mr {self.fname}"
        
#         elif self.gender == "Female":
#             return f"Hello Miss {self.fname}"
        
#         else:
#             return f"Hello {self.fname}"


#     def get_all_info(self) :
        
#         return f"{self.name_with_title()}, Your Full Name Is: {self.get_full_name()}"





# member_one = Member("Abdullah", "Khaled", "Alakel", "Male")
# member_two = Member("Abode", "Samer", "Jalal", "Male")
# member_three = Member("Wifi", "Maya", "Tahseen", "Female")


# print(dir(member_one))   # Here you Gonna See name (inside Attributes)

# print(member_one.fname, member_one.mname, member_one.lname)     # Abdullah Khaled Alakel
# print(member_two.fname, member_two.mname, member_two.lname)     # Abode Samer Jalal
# print(member_three.fname, member_three.mname, member_three.lname)   # Wifi Maya Tahseen



# print(member_one.get_full_name())   # Abdullah Khaled Alakel
# print(member_two.get_full_name())    # Abode Samer Jalal
# print(member_three.get_full_name())    # Wifi Maya Tahseen



# print(member_one.name_with_title())    # Hello Mr Abdullah
# print(member_three.name_with_title())    # Hello Miss Wifi




# print(member_one.get_all_info())    # Hello Mr Abdullah, Your Full Name Is: Abdullah Khaled Alakel
# print(member_three.get_all_info())    # Hello Miss Wifi, Your Full Name Is: Wifi Maya Tahseen

print("-------------------------------------------------")
#-------------------------------------------------------------
print("-------------------------------------------------")

# OOP => Class Attributes:

# Class Attributes: Attributes Defined OutSide the Constructor


# class Member:

#     not_allowed_names = ["Hell", "Shit", "Fuck"]      ## Class Attribute defined outside the Constructor

#     users_number = 0

#     def __init__(self, first_name, middle_name, last_name, gender) :    # Important Note: Instance Attributes will be Inside Constructor

#         self.fname = first_name
#         self.mname = middle_name
#         self.lname = last_name
#         self.gender = gender
#         Member.users_number += 1

#     def get_full_name(self) :
#         if self.fname in Member.not_allowed_names:

#             raise ValueError("Name Not Allowed!")
        
#         else:

#             return f"{self.fname} {self.mname} {self.lname}"


#     def name_with_title(self) :

#         if self.gender == "Male":
#             return f"Hello Mr {self.fname}"
        
#         elif self.gender == "Female":
#             return f"Hello Miss {self.fname}"
        
#         else:
#             return f"{self.fname}"


#     def get_all_info(self) :
        
#         return f"{self.name_with_title()}, Your Full Name Is: {self.get_full_name()}"


#     def delete_user(self) :

#         Member.users_number -= 1

#         return f"User {self.fname} Deleted. "
# # print(dir(Member))   ## Here We gonna find that the class attributes and the instance methods will be appear here but the instance attributes will not appear here

# print(Member.users_number)   # 0

# member_one = Member("Abdullah", "Khaled", "Alakel", "Male")
# member_two = Member("Shit", "Samer", "Jalal", "Male")
# member_three = Member("Wifi", "Maya", "Tahseen", "Female")

# print(Member.users_number)    # 3


# print(member_one.get_all_info())   # Run Normal And proceed without any issues
# # print(member_two.get_all_info())   # Value Error: Name Not Allowed!!

# print(member_two.delete_user()) # User Shit Deleted.

# print(Member.users_number)   # 2

#-------------------------------------------------------------


# OOP => Class Methods , Static Methods

# Class Methods:
# 1- Marked With @classmethod Decorator to Flag it as Class Method
# 2- it takes Cls Parameter Not Self to point to the class Not the Instance
# 3- It Doesn't Require Creation of a Class Instance
# 4- Used When You Want to Do Something With the Class Itself


# Static Methods:
# 1- It takes No Parameters
# 2- Its Bound To the Class Not Instance
# 3- Used WHen Doing Something Doesn't Have Access to Object Or Class But Related To Class


# class Member:

#     not_allowed_names = ["Hell", "Shit", "Fuck"]      ## Class Attribute defined outside the Constructor

#     users_number = 0

#     @classmethod
#     def show_users_count(cls) :     # Class Method must be have cls not self

#         print(f"We Have {cls.users_number} Users In Our App")

#     @staticmethod
#     def say_hello() :      # Static Method it can be without Parameter,,, it related to the class 

#         print("Hello From Static Method")


#     def __init__(self, first_name, middle_name, last_name, gender) :    # Important Note: Instance Attributes will be Inside Constructor

#         self.fname = first_name
#         self.mname = middle_name
#         self.lname = last_name
#         self.gender = gender
#         Member.users_number += 1

#     def get_full_name(self) :
#         if self.fname in Member.not_allowed_names:

#             raise ValueError("Name Not Allowed!")
        
#         else:

#             return f"{self.fname} {self.mname} {self.lname}"


#     def name_with_title(self) :

#         if self.gender == "Male":
#             return f"Hello Mr {self.fname}"
        
#         elif self.gender == "Female":
#             return f"Hello Miss {self.fname}"
        
#         else:
#             return f"{self.fname}"


#     def get_all_info(self) :
        
#         return f"{self.name_with_title()}, Your Full Name Is: {self.get_full_name()}"


#     def delete_user(self) :

#         Member.users_number -= 1

#         return f"User {self.fname} Deleted. "
# # print(dir(Member))   ## Here We gonna find that the methods inside instance will be appear here

# print(Member.users_number)   # 0

# member_one = Member("Abdullah", "Khaled", "Alakel", "Male")
# member_two = Member("Shit", "Samer", "Jalal", "Male")
# member_three = Member("Wifi", "Maya", "Tahseen", "Female")

# print(Member.users_number)    # 3


# print(member_one.get_all_info())   # Run Normal And proceed without any issues
# # print(member_two.get_all_info())   # Value Error: Name Not Allowed!!

# print(member_two.delete_user()) # User Shit Deleted.

# print(Member.users_number)   # 2


# Member.show_users_count()   # We Have 2 Users In Our App

# ## below important to under stand that we wrote the first one below but python in the background will make in the second line, so both same result
# print(member_one.get_full_name())   # Abdullah Khaled Alakel
# print(Member.get_full_name(member_one))   # Abdullah Khaled Alakel

# Importan: print(Member.get_full_name(member_one))  / here in the back ground called class then method then it will put the instance that
# you create from the class



# Member.say_hello()   # Hello From Static Method    (Run the static Method)


#-------------------------------------------------------------
print("-------------------------------------------------")
#-------------------------------------------------------------
print("-------------------------------------------------")


## OOP => Magic Methods:

#1-  Everything In Python Is An Object
#2-  __init__ Called Automatically When Instantaiting the Class
#3-  Self.__class__ the class to which a class instance belongs
#4-  __str__ Gives a Human-Readable output of the Object
#5- __len__ Returns the length of the container
#           Called when we use the built-in len() function on the object

# Example:

class skill:

    def __init__(self):    ## define constructor here

        self.skills = ["HTML", "CSS", "JS"]


    def __str__(self):     ## __str__ Magic Method it returns Human Readable msg (Contains info about this object)

        return f"This Is my Skills => {self.skills}"

    def __len__(self) :

        return len(self.skills)

my_profile = skill()

print(my_profile)   # <__main__.skill object at 0x000002109B559C50>

print(len(my_profile))   # Error  object of type 'skill' has no len()  becasue you didn't use magic method __len__ inside your class

# after add __len__ inside the class it return a result of   ##### 3


my_profile.skills.append("Python")   # we add new skills to check if len will add on the len and change the old number
my_profile.skills.append("Go")      # # we add new skills to check if len will add on the len and change the old number

print(len(my_profile))   # 5         so the result change from 3 to 5 


# print(my_profile.__class__)   # <class '__main__.skill'>  here it means that my_profile(Instance) is related to the class name skill



# Another Example:

# my_string = "Alakel"

# print(type(my_string))   # <class 'str'>  here we can understand that it's related to the str class

# print(my_string.__class__)  # <class 'str'> str is class and has methods inside it 

# print(dir(str))  # it will show all methods inside class str

# print(str.upper(my_string))  # ALAKEL


# print("-------------------------------------------------")

# Another Example: 

# my_num = 12   # here in background.... you make instantiate for class int and you create instance under name my_num

# print(type(my_num))      # <class 'int'>
# print(my_num.__class__)  # <class 'int'>

# print(dir(int))   ## here you gonna see the methods and magic methods inside int class
# print("-------------------------------------------------")
# print(dir(float)) # here you gonna see the methods and magic methods inside float class
# print("-------------------------------------------------")
# print(dir(type)) # here you gonna see the methods and magic methods inside type class
print("-------------------------------------------------")
print("-------------------------------------------------")
print("-------------------------------------------------")

## OOP => Inheritance 



# class Food:   # Base Class

#     def __init__(self, name, price):
        
#         self.name = name
#         self.price = price

#         print(f"{self.name} Is Created From Base Class")

#     def eat(self):

#         print("Eat Method From Base Class")



# class Apple(Food):  # Apple is Derived Class and to inherit from the base class we put it Apple()

#     def __init__(self, name, price, amount):     # this constructor is overwrite on the main class constructor even if it's inherit
#                                         # with super() means you want take attributes from the base class 


#         # Food.__init__(self, name)     # Create Instance from Base Class     this line is same the line below (same action will do)
#         super().__init__(name, price)  # Here if you want to inherit only one attribute super"to donot write the class name.__init__"(attribute)

#         self.amount = amount    # this attribute not get from base class we create it here

#         print(f"{self.name} Is Created From Derived Class and price is {self.price} and amount is {self.amount}")  

#     def get_from_tree(self):

#         print("Get From Tree From Derived Class")


# # food_one = Food("Pizza")
# food_two = Apple("Pizza", 150, 600)    # Pizza Is Created From Derived Class and price is 150
# food_two.eat()    # Eat Method From Base Class
# food_two.get_from_tree()  # Get From Tree From Derived Class

print("-------------------------------------------------")

# OOP => Multiple Inheritance , Method overwrite, MRO : Method Resolution Order

# Method Overwrite:


# when you have two classes (base class that you inherit from it) and the derived class that take from the base class
# so to overwrite you can write the same name function in the derived class so it will overwrite in this way


#Multiple Inheritance:


# class BaseOne:
    
#     def __init__(self):

#         print("Base One")

#     def fun_one(self):

#         print("One")


# class BaseTwo:

#     def __init__(self):

#         print("Base Two")
    
#     def fun_two(self):

#         print("two")


# class Dervied(BaseOne, BaseTwo):


#     pass


# my_var = Dervied()   # Base One 

# # below you can know the order and what is the order to run first and last:
# # through method resoltion order  mro()
# # print(Dervied.mro())   # [<class '__main__.Dervied'>, <class '__main__.BaseOne'>, <class '__main__.BaseTwo'>, <class 'object'>]




# print(my_var.fun_one)  # <bound method BaseOne.fun_one of <__main__.Dervied object at 0x0000021A5B006790>>
# print(my_var.fun_two)  # <bound method BaseTwo.fun_two of <__main__.Dervied object at 0x0000021A5B006790>>

# my_var.fun_one()  # One
# my_var.fun_two()  # two

#############################
# The example below to understand the Multiple inhertiance
# class Base:

#     pass


# class DerivedOne(Base):   # the class DerivedOne Take Attributes from Class Base ( Inherit)

#     pass


# class DerivedTwo(DerivedOne): # the class DereivedTwo Take Attribute from Class DerivedOne(Inherit) and also from Base becasuse of DerivedOne
#                                 # already inherit it's attributes from class base 

#     pass


print("-------------------------------------------------")


# OOP => Polymorphism    =====>>>> Mini forms تعدد الاوجه
# same method do a specific action and in another place will do another action
n1 = 10
n2 = 20

print(n1 + n2)   # 30

s1 = "Hello"
s2 = "Python"

print(s1 + " " + s2)   # Hello Python


print(len([1,2,3,4,5,6]))   # 6   the number of elements inside list 

print(len("Abdullah Alakel"))  #  15   characters number

print(len({"Key_one": 1, "Key_two": 2}))  # 2    number of the keys


# THe Idea of Polymorphism: that same method in different places make different actions


class A:

    def do_somthing(self):

        print("From Class A")

        raise NotImplementedError("Derived Class Must Implement this Method") # because of this raise will push the other drived classes to implement this method inside each class


class B(A):

    def do_somthing(self):

        print("From Class B")



class C(A):

    def do_somthing(self):

        print("From Class C")


my_instance = B()

my_instance.do_somthing() 


#### Above we gonna see method under name do_somthing in each place do somthing different because of raise Error NotImplementedError

# so here we saw the polymorphism, same method name but do different actions 


print("-------------------------------------------------")


# OOP => Encapsulation

# Encapsulation:

# 1- Restrict access to the data Stored in attributes and methods inside the class

# public
# 2- Every Attribute and Method that we used so far is public
# 3- Attributes and methods can be modified and run from everywhere
# 4- Inside Or OutSide the class

# Protected
# 5- Attributes and Methods Can be Accessed from within the class and sub classes that means the derived classes
# 6- attributes and Methods prefixed with one underscore _
# Python don't have this !!!!!!!!!!!!!!!!!!!!

# Private
# 7- Attributes and Methods Can be Accessed from within the class or Object only 
# 8- Attributes cannot be Modified from outside the class
# 9- Attributes and Methods Prefixed with two underscores __ 


# Attributes = Variables = Properties   these three calls are same even in other websites information

# 1- Public

# class Member:

#     def __init__(self, name):
#         self.name = name    # Public 

# one = Member("Alakel")

# print(one.name)

# one.name = "Abdullah"  you can Edit without any issue because it's public

# print(one.name)


print("-------------------------------------------------")


# Protected , still you can call it and edit on it, so the _ before the property is only to refference for the person that it'S protected 

# class Member:

#     def __init__(self, name):
#         self._name = name    # Protected 

# one = Member("Alakel")

# print(one._name)

# one._name = "Abdullah"  

# print(one._name)


print("-------------------------------------------------")


# Private

# class Member:

#     def __init__(self, name):
#         self.__name = name    # Private property 

#     def say_hello(self):

#         return f"Hello {self.__name}"


# one = Member("Alakel")
# # print(one.__name)   #Error   AttributeError: 'Member' object has no attribute '__name'
# print(one.say_hello())   # Hello Alakel

# print(one._Member__name)  # Alakel    it will print too even if private so the private it will be note for the developers that you work with
# #                                        ## it's not a really restrected as a private or protected!!


print("-------------------------------------------------")

### OOP => Getters and Setters

# Getter : will get a specific data
# Setter: will set a specific data (new data, edit on previous data...)


# class Member:

#     def __init__(self, name):

#         self.__name = name    # Private

#     def say_hello(self):

#         return f"Hello {self.__name}"
    
#     def get_name(self):   ## Getter 

#         return self.__name


#     def set_name(self, new_name) :  ## Setter
        
#         self.__name = new_name

# one = Member("Alakel")

# print(one.get_name())   # Alakel


# one.set_name("Abode")

# print(one.get_name())   # Abode



print("-------------------------------------------------")

## OOP => @Property Decorator:
# This decorator will change the function from function to a property so if you see below how you call it same the way to call the property not a function becuase we will get an error
# class Member:

#     def __init__(self, name, age):

#         self.name = name

#         self.age = age

#     def say_hello(self):

#         return f"Hello {self.name}"
    
#     @property
#     def age_in_days(self):    ## if you have method but without parameter only self and not action will did it's only return a result simple

#         return self.age * 365    
    



# one = Member("Alakel", 25)

# print(one.name)   # Alakel
# print(one.age)    # 25
# print(one.say_hello())   # Hello Alakel
# # print(one.age_in_days())   # 9125  now after add @property before the method so it will return an Error TypeError: 'int' object is not callable

# print(one.age_in_days)  # 9125 now it will work without any issue because it's behavior same the property not method 


print("-------------------------------------------------")

### OOP => ABCs => Abstract Base Class

# Class Called Abstract Class if it has one or more Abstract Method
# abc Module in python provides Infrastructure for defining custom Abstract Base Classes
# BY Adding @absttractmethod Decorator on the Methods
# ABCMeta Class Is a Metaclass Used for Defining Abstract Base Class

# لللفهم هنا لاجل عمل كلاس ابستراكت بمعنى مجرد و اضافة ابستراكت ميثودز بمعنى مجردة لاجل الاكلاسات الاخرى تلحق هذا الباترن و تلتزم بعمل هذه الميثودز بداخلها 
# اي ان الكلاس ابستراكت يكون بمعنى ستاندرد لباقي الكلاسات و المثال التالي يوضح ذلك

# from abc import ABCMeta, abstractmethod     ## must make import to use Abstract Base Classes


# class Programming(metaclass=ABCMeta):  # with adding (metaclass=ABCMeta) so that i want this class to be abstract base class for other classes that inherit from him

#     @abstractmethod
#     def has_oop(self):       ## this method with the decorator before it tell that this method is abstract

#         pass
    

#     @abstractmethod
#     def has_name(self):      ## this method is abstract method

#         pass

# class Python(Programming):     ## class python inherit from programming class and programming class is abstract base class

#     def has_oop(self):

#         return "Yes"
    
#     def has_name(self):

#         pass


# class Pascal(Programming):  ## class pascal inherit from programming class and programming class is abstract base class

#     def has_oop(self):

#         return "No"
    
#     def has_name(self):

#         pass


# one = Python()
# two = Pascal()

# print(one.has_oop())  # Yes
# print(two.has_oop())  # No


print("-------------------------------------------------")
print("-------------------------------------------------")
# print("-------------------------------------------------")
# print("-------------------------------------------------")

### Important for random module 
import random

print(f'A random float between 0 & 1.0: {random.random()}')    # A random float between 0 & 1.0: 0.6108611262269857
print(f'A random int between 0 & 10: {random.randrange(11)}')    # A random int between 0 & 10: 1
print('A random choice from a list: ' + random.choice(['paper', 'scissors', 'rock']))   # A random choice from a list: scissors
deck = ['hearts', 'diamonds', 'spades', 'clubs']
random.shuffle(deck)
print(deck)   # ['hearts', 'spades', 'diamonds', 'clubs']



print("-------------------------------------------------")
print("-------------------------------------------------")
# print("-------------------------------------------------")
# print("-------------------------------------------------")

# DATABASE SECTION    IMPORTANT
