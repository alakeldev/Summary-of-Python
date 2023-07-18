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

