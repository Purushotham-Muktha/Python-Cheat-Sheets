msg = "Hello world!" 
print(msg) 


print("Hello! Python is interpreter Language")
###########################
##  Python reserved keywords and built-in functions comes from standard  python Packaging Libraries----THEY SHOULD NOT BE USED AS VARIABLES
###########################

'''python --version

# Python KEYWORDS

False     True      await     else      import    pass      None      break     except    in   raise
class     finally   is        return     and     continue   for       lambda     try      as   def  
from      nonlocal  while     assert    del      global     not       with       async    elif  if  
or   
yield     


# PYTHON BUILT-IN FUNCTIONS

print()        all()     complex()      hash()         min()       slice()    abs()      aiter()
delattr()      help()      next()       sorted()       dict()      hex()      object()   staticmethod( )
any()          dir()       id()         oct()          str()       anext()     divmod()    input()       
open()         sum()         int()     ascii()       enumerate()    ord()     super()      type()    
bin()          eval()    isinstance()   pow()          tuple()        bool()    exec()    issubclass()      
filter()       iter()    property()     vars()          bytearray()    float()   len()     range()   zip()      
format()       list()    repr()         _import_()      callable()          frozenset()     locals()
reversed()     chr()     getattr()      map()         round()         classmethod()  
globals()      max()     set()          compile()      hasattr()      memoryview()        setattr()
breakpoint()  bytes()
 
'''


import this

msg="Hello! python is future "
print("Hello! python is interpreter language")
print(msg.upper())
print(msg.lower())
print(msg.title())


a="Puru"
b="Muktha"
fullname=f"{a}\t {b}"
print(fullname)
print(f"Hello!, {fullname.title()}")
print(f"Hello!, {fullname.lower()}")
print(f"Hello!, {fullname.upper()}")
message=f"Hello!, {fullname.title()}"
print(message)
print( "\t" + message)
print( "\n" + message)

# \t tab space
# \n new line space

#Striping Whitespaces   -- Removing the blank spaces of  variable values from LEFT or RIGHT Or EXACT Display

name="PYTHON "
name1=" JAVA"
name2=" C-Language base "
print(name.rstrip())
print(name1.lstrip())
print(name2.strip())

print(name2.rstrip())
print(name1.lstrip())
print(name.strip())

print(name1.rstrip())
print(name2.lstrip())
print(name1.strip())

web='https://www.purutech.com'
print(web.removeprefix('https://'))

import this

msg="Hello! python is future "
print("Hello! python is interpreter language")
print(msg.upper())
print(msg.lower())
print(msg.title())


print("\n simple function \n")
def addsomething(x,y):
    #return x + y
    #return x - y
    return x * y
    return x / y
    return x % y
    return x ^ y
print("The value of z: ", addsomething(5,8))

import datetime
print(datetime.datetime.now())

del str

print(str(datetime.datetime.now().date()))


myVar = 5
print(myVar)

Test = 0b100
print("100 Binary: ", Test)

Test = 0o100
print("100 Octal: ", Test)

Test = 100
print ("100 Decimal: ", Test)

Test = 0x100
print("100 Hexadecimal:", Test)

print(bin(Test))
print(oct(Test))
print(hex(Test))

Test = 255.0
print("Direct Assignment: ", Test)

Test = 2.55e2
print("Scientific Notation: ", Test)

Test = 2.55e-2
print("Negative Exponent: ", Test)

myComplex = 3 + 4j
print("Real Part: ", myComplex.real)
print("Imaginary Part: ", myComplex.imag)

myBool = 1 > 2
print("Is 1 > 2? ", myBool)

myInt = 5
print(type(myInt))

print(ord("A"))

myInt = int("123")
print(myInt)

print(type(myInt))

myStr = str(1234.56)
print(myStr)
print(type(myStr))



def get_values():
    yield 42
    yield 'hello'
    yield [1, 2, 3]
 
# Test code
result = get_values()
print(next(result))  # should print 42
print(next(result))  # should print 'hello'
print(next(result))  # should print [1, 2, 3]


first_name = 'albert' 
last_name = 'einstein'
full_name = first_name + ' ' + last_name 
print(full_name) 

bikes = ['trek', 'redline', 'giant'] 
first_bike = bikes[0] 
last_bike = bikes[-1] 
print(bikes[0])
print(bikes[-1])
print(bikes[2])

for bike in bikes:   
      print(bike) 

bikes = []
bikes.append('trek') 
bikes.append('redline') 
bikes.append('future is python lanaguage') 
bikes.append('giant') 
print(bikes)

squares = []
for x in range(1, 11): 
       squares.append(x**2) 
print(squares)

squares = [x**2 for x in range(1, 11)] 
print(squares)

finishers = ['sam', 'bob', 'ada', 'bea'] 
first_two = finishers[:2] 
print(first_two)

copy_of_bikes = bikes[:] 

print(copy_of_bikes)

#tuples
dimensions = (1920, 1080) 
print(dimensions)

thistuple = ("apple", "banana", "cherry")
print(thistuple)

# if statements
#age=print(input("Enter your age: "))
#print(age)

age=16

if age > 18:     
    print("You can vote!", age) 
else:
    print("You are not eligible to vote:",  age) 

age=5 

if age < 4:    
     ticket_price = 0
elif age < 18:    
     ticket_price = 10 
else:     
     ticket_price = 15 
print(ticket_price)

alien = {'color': 'green', 'points': 5} 
print("The alien's color is " + alien['color']) 

alien['x_position'] = 0 
fav_numbers = {'eric': 17, 'ever': 4} 
for name, number in fav_numbers.items():    
     print(name + ' loves ' + str(number)) 


     fav_numbers = {'eric': 17, 'ever': 4} 
     for name in fav_numbers.keys():   
         print(name + ' loves a number') 

fav_numbers = {'eric': 17, 'ever': 4} 
for number in fav_numbers.values():    
 print(str(number) + ' is a favorite') 


 #Prompting for a value
name = input("What's your name? ")
print("Hello, " + str(name) + "!") 

 #Prompting for numerical input 
age = int(input("How old are you? "))
 #age = int(age)  
print(age)

pi = input("What's the value of pi? ")
pi = float(pi) 
print(str(pi))

msg = '' 
while msg != 'quit': 
    msg = input("What's your message? ") 
    print(msg)



# Creating and Using Functions

# 2.	Type def Hello(): and press Enter.
def Hello():
    # 3.	Type print(“This is my first Python function!”)
    print("This is my first Python function!")

# Accessing the defined functions

Hello()

#Sending information to functions
 #   Understanding arguments
 

def Hello2( Greeting ):
    print(Greeting)

# Sending required arguments
Hello2("This is an interesting function.")
Hello2("Another message...")

Hello2(1234)
Hello2(5 + 5)

#Sending arguments by keyword
def AddIt(Value1, Value2):
    print(Value1, " + ", Value2, " = ", (Value1 + Value2))

AddIt(2, 3)
AddIt(Value2 = 3, Value1 = 2)
# Giving function arguments a default value

def Hello3(Greeting = "No Value Supplied"):
    print(Greeting)
    Hello3()

Hello3("This is a string")
Hello3(5)
Hello3(2 + 7)

#Creating functions with a variable number of arguments
def Hello4(ArgCount, *VarArgs):
    print("You passed ", ArgCount, " arguments.")
    for Arg in VarArgs:
       print(Arg)

Hello4(1, "A Test String.")
Hello4(3, "One", "Two", "Three")

#Returning information from functions
def DoAdd(Value1, Value2):
    return Value1 + Value2
print("The sum of 3 + 4 is ", DoAdd(3,4))

#Comparing function output
print("3 + 4 equals 2 + 5 is ", (DoAdd(3,4)==DoAdd(2,5)))

#Making Simple Decisions Using the if Statement
TestMe = 6
if TestMe == 6:
   print("TestMe does equal 6!")
   print("All done!")

#   Making multiple comparisons using logical operators
Value = int(input("Type a number between 1 and 10: "))
if (Value > 0) and (Value <= 10):
   print("You typed: ", Value)

#Type a number between 1 and 10: 5
#You typed:  5

Value = int(input("Type a number between 1 and 10: "))
if (Value > 0) and (Value <= 10):
   print("You typed: ", Value)

#Type a number between 1 and 10: 22
Value = int(input("Type a number between 1 and 10: "))
if (Value > 0) and (Value <= 10):
   print("You typed: ", Value)
   
   
#Choosing Alternatives Using the if...else Statement
#Using the if...else statement in an application
Value = int(input("Type a number between 1 and 10: "))
if (Value > 0) and (Value <= 10):
   print("You typed: ", Value)
else:
   print("The value you typed is incorrect!")
   
#Using the if...elif statement in an application
print("1. Red")
print("2. Orange")
print("3. Yellow")
print("4. Green")
print("5. Blue")
print("6. Purple")
Choice = int(input("Select your favorite color: "))
if (Choice == 1):
   print("You chose Red!")
elif (Choice == 2):
   print("You chose Orange!")
elif (Choice == 3):
   print("You chose Yellow!")
elif (Choice == 4):
   print("You chose Green!")
elif (Choice == 5):
   print("You chose Blue!")
elif (Choice == 6):
   print("You chose Purple!")
else:
   print("You made an invalid choice!")

#Using Nested Decision Statements
#Using multiple if or if...else statements

One = int(input("Type a number between 1 and 10: "))
Two = int(input("Type a number between 1 and 10: "))
if (One >= 1) and (One <= 10):
   if (Two >= 1) and (Two <= 10):
      print("Your secret number is: ", One * Two)
   else:
      print("Incorrect second value!")
else:
   print("Incorrect first value!")

#Combining other types of decisions

print("1. Eggs")
print("2. Pancakes")
print("3. Waffles")
print("4. Oatmeal")
MainChoice = int(input("Choose a breakfast item: "))
if (MainChoice == 2):
   Meal = "Pancakes"
elif (MainChoice == 3):
   Meal = "Waffles"
if (MainChoice == 1):
   print("1. Wheat Toast")
   print("2. Sour Dough")
   print("3. Rye Toast")
   print("4. Pancakes")
   Bread = int(input("Choose a type of bread: "))
   if (Bread == 1):
      print("You chose eggs with wheat toast.")
   elif (Bread == 2):
      print("You chose eggs with sour dough.")
   elif (Bread == 3):
      print("You chose eggs with rye toast.")
   elif (Bread == 4):
      print("You chose eggs with pancakes.")
   else:
      print("We have eggs, but not that kind of bread.")
elif (MainChoice == 2) or (MainChoice == 3):
   print("1. Syrup")
   print("2. Strawberries")
   print("3. Powdered Sugar")
   Topping = int(input("Choose a topping: "))
   if (Topping == 1):
      print ("You chose " + Meal + " with syrup.")
   elif (Topping == 2):
      print ("You chose " + Meal + " with strawberries.")
   elif (Topping == 3):
      print ("You chose " + Meal + " with powdered sugar.")
   else:
      print ("We have " + Meal + ", but not that topping.")
elif (MainChoice == 4):
   print("You chose oatmeal.")
else:
   print("We don't serve that breakfast item!")


#Processing Data Using the for Statement
#Creating a basic for loop

LetterNum = 1
for Letter in "Howdy!":
   print("Letter ", LetterNum, " is ", Letter)
   LetterNum+=1

#Controlling execution with the break statement

Value = input("Type less than 6 characters: ")
LetterNum = 1
for Letter in Value:
   print("Letter ", LetterNum, " is ", Letter)
   LetterNum+=1
   if LetterNum > 6:
      print("The string is too long!")
      break
  
#Controlling execution with the continue statement
LetterNum = 1
for Letter in "Howdy!":
   if Letter == "w":
      continue
      print("Encountered w, not processed.")
   print("Letter ", LetterNum, " is ", Letter)
   LetterNum+=1


#Doing nothing with the pass statement
LetterNum = 1
for Letter in "Howdy!":
   if Letter == "d":
      pass #Add some code here later to process w
   print("Letter ", LetterNum, " is ", Letter)
   LetterNum+=1

#Validating input with the else statement
Value = input("Type less than 6 characters: ")
LetterNum = 1
for Letter in Value:
  print("Letter ", LetterNum, " is ", Letter)
  LetterNum+=1
  if (Letter == "" or Letter == Value[-1]):
    break
else:
  print("The string is blank.")

#Processing Data Using the while Statement
#Using the while statement in an application

Sum = 0
while Sum < 5:
   print(Sum)
   #Sum+=1
   Sum=Sum+1

#Nesting Loop Statements

X = 1
Y = 1
print ('{:>4}'.format(' '), end= ' ')
for X in range(1, 20):
   print('{:>4}'.format(X), end=' ')
print()
for X in range(1,20):
   print('{:>4}'.format(X), end=' ')
   while Y <= 20:
      print('{:>4}'.format(X * Y), end=' ')
      #Y+=1
      Y=Y+1
   print()
   Y=1
   
   
 #Catching Exceptions
#Basic exception handling
#Handling a single exception
try:
   Value = int(input("Type a number between 1 and 10: "))
except ValueError:
   print("You must type a number between 1 and 10!")
else:
   if (Value > 0) and (Value <= 10):
      print("You typed: ", Value)
   else:
      print("The value you typed is incorrect!")

#Using the except clause without an exception
try:
   Value = int(input("Type a number between 1 and 10: "))
except ZeroDivisionError:
   print("This is the generic error!")
except ValueError:
   print("You must type a number between 1 and 10!")
else:
   if (Value > 0) and (Value <= 10):
      print("You typed: ", Value)
   else:
      print("The value you typed is incorrect!")

#Working with exception arguments
import io
import sys
try:
   File = open("c:/Users/pmuktha/OneDrive - Capgemini/Desktop/01 Purushotham/02 Education/Python Programing Language/if.py")
except IOError as e:
   print("Error opening file!\r\n" +
      "Error Number: {0}\r\n".format(e.errno) +
      "Error Text: {0}".format(e.strerror))
else:
   print("File opened as expected.")
   File.close()

#Sidebar: Obtaining a list of exception arguments

import sys
try:
   File = open("myfile.txt")
except IOError as e:
   for Entry in dir(e):
      if (not Entry.startswith("_")):
         try:
            print(Entry, " = ", e.__getattribute__(Entry))
         except AttributeError:
            print("Attribute ", Entry, " not accessible.")
else:
   print("File opened as expected.")
   File.close()

#Handling multiple exceptions with a single except clause
try:
   Value = int(input("Type a number between 1 and 10: "))
except (ValueError, KeyboardInterrupt):
   print("You must type a number between 1 and 10!")
else:
   if (Value > 0) and (Value <= 10):
      print("You typed: ", Value)
   else:
      print("The value you typed is incorrect!")

#Handling multiple exceptions with multiple except clauses
try:
   Value = int(input("Type a number between 1 and 10: "))
except ValueError:
   print("You must type a number between 1 and 10!")
except KeyboardInterrupt:
   print("You pressed Ctrl+C!")
else:
   if (Value > 0) and (Value <= 10):
      print("You typed: ", Value)
   else:
      print("The value you typed is incorrect!")

#Handling more specific to less specific exceptions
try:
   Value1 = int(input("Type the first number: "))
   Value2 = int(input("Type the second number: "))
   Output = Value1 / Value2
except ValueError:
   print("You must type a whole number!")
except KeyboardInterrupt:
   print("You pressed Ctrl+C!")
except ArithmeticError:
   print("An undefined math error occurred.")
except ZeroDivisionError:
   print("Attempted to divide by zero!")
else:
   print(Output)

try:
   Value1 = int(input("Type the first number: "))
   Value2 = int(input("Type the second number: "))
   Output = Value1 / Value2
except ValueError:
   print("You must type a whole number!")
except KeyboardInterrupt:
   print("You pressed Ctrl+C!")
except ZeroDivisionError:
   print("Attempted to divide by zero!")
except ArithmeticError:
   print("An undefined math error occurred.")
else:
   print(Output)

#Nested exception handling
TryAgain = True
while TryAgain:
   try:
      Value = int(input("Type a whole number. "))
   except ValueError:
      print("You must type a whole number!")
      try:
         DoOver = input("Try again (y/n)? ")
      except:
         print("OK, see you next time!")
         TryAgain = False
      else:
         if (str.upper(DoOver) == "N"):
            TryAgain = False
   except KeyboardInterrupt:
      print("You pressed Ctrl+C!")
      print("See you next time!")
      TryAgain = False
   else:
      print(Value)
      TryAgain = False

#Raising Exceptions
#Raising exceptions during exceptional conditions

try:
   raise ValueError
except ValueError:
   print("ValueError Exception!")

#Passing error information to the caller
try:
   Ex = ValueError()
   Ex.strerror = "Value must be within 1 and 10."
   raise Ex
except ValueError as e:
   print("ValueError Exception!", e.strerror)

#Deciding to Say “Oops” in Your Own Way: Custom Exceptions
class CustomValueError(ValueError):
   def __init__(self, arg):
      self.strerror = arg
      self.args = {arg}
try:
   raise CustomValueError("Value must be within 1 and 10.")
except CustomValueError as e:
   print("CustomValueError Exception!", e.strerror)

#Using the finally Clause
import sys
try:
   raise ValueError
   print("Raising an exception.")
except ValueError:
   print("ValueError Exception!")
   sys.exit()
finally:
   print("Taking care of last minute details.")
print("This code will never execute.")

#Importing Packages
#Sidebar: INTERACTING WITH THE CURRENT PYTHON DIRECTORY
import os
print(os.getcwd())
for entry in os.listdir(): 
    print(entry)


#Finding Packages
#Locating packages on disk
import sys
for p in sys.path: print(p)

import os
os.environ['PATH'].split(os.pathsep)
sys.path.append(os.getcwd())
for p in sys.path: print(p)

#!echo %PYTHONPATH%   ## Windows
#!echo $PTYHONPATH    ## Linux and macOS

#Downloading Packages from Other Sources
#Installing packages by using pip
#!pip list --outdated

#Installing packages using the %pip magics
#%pip list --outdated