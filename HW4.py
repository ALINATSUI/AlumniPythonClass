#Exercise 34.

#1) Can you explain why the year 2010 in "January 1, 2010" really is 2010 and not 2009?
"""2000 = 0
2001 = 1
2002= 2
2003= 3
2004 = 4
2005 = 5
2006 = 6
2007 = 7
2008 = 8
2009 = 9
2010 = 10"""

year = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010]

year[0] = 2000
year[1] = 2001
year[2] = 2002
year[3] = 2003
year[4] = 2004
year[5] = 2005
year[6] = 2006
year[7] = 2007
year[8] = 2008
year[9] = 2009 
year[10] = 2010

#2) Write some more lists and work out similar indexes until you can translate them.

lovlies = ['confidence', 'authenticity', 'good friends', 'work in progress']

#The second lovlies
#The lovlies at 4th position
#The lovlies at 3rd position
#The first lovlies

print(lovlies[1]) #'authenticity'
print(lovlies[3]) #'work in progress'
print(lovlies[2]) #'good friends'
print(lovlies[0]) #'confidence'



#1) how many seconds are there in 42 minutes 42 seconds?

#60 seconds * 1 minute = #of seconds
seconds = 60*42+42
print(seconds)


#2) How many miles are there in 10 kilometers? 1.61 km = 1 miles

#10*1.61 = #of miles

miles = 10*1.61
print(miles)

#3) How much is 83 degrees Fahrenheit in degree celsius?

#celsius = 32degrees Fahrenheit
celsius = (83-32)*5/9
print(f"The temperature in celsius is: {celsius}")


#4) import math library and find the square root of numbers 81, 19, 16, 121
import math

#setting a function with 4 parameters
def finding_the_square_root(num1,num2,num3,num4):

    value1 = math.sqrt(int(num1))
    value2 = math.sqrt(int(num2))
    value3 = math.sqrt(int(num3))
    value4 = math.sqrt(int(num4))
    print(f"The square root of {num1} is {value1}.\nThe square root of {num2} is {value2}.\nThe square root of {num3} is {value3}.\nThe square root of {num4} is {value4}.")
    """for x in finding_the_square_root:
        return math.sqrt(x) ???"""
finding_the_square_root(81,19,161,121)


#5) write a program that returns the area of a circle

#import math
r = 9

Area_of_A_circle = int(math.pi*(r*r))
print(f"The area of the circle is: {Area_of_A_circle}")

#6) write a boolean function that returns true or false if the letter x is
#in a string provided by the user








def letterletter():
    question = input("Enter in a phrase: ")
    word = list(question)
    for i in word:
        if(i == 'x'):
            return True
        else:
            return False

letterletter()

#7) write a boolean function that returns true or false if any of the letter
#i a,e,i,o, u and in a string provided by the user




#8) What is the volume of a sphere with radius 5? The volume of a sphere with radius r is  (4/3)πr3
#import math
volume = (4/3)*math.pi*r**3
r = 5
print(f"The volume of the sphere is: {volume}")

#9). Write a boolean function that returns true if a given input is divisible by 3 or return false otherwise

question = int(input("Enter a number: "))
divisible = question%3


"""if({divisible} == 0):
    print(f"the number you entered is divisible by 3")
else:
    print(f"the number you entered is not divisible by 3")"""

def divisibility(x):
    no = False
    if({divisible} == 0):
        print("Yes")
        return True
    else:
        print("no")
        return False
divisibility({divisible})



#10). Import data/time library and print out today's date and current time

import datetime
import time

Current_date_and_time = datetime.datetime.now()
print(f"Today's date and time is: {Current_date_and_time}")

#11). using the data time library, print out the current year
"""import datetime
import time"""
current_year = datetime.datetime.now().year
print(f"The current year is: {current_year}")

#12). write a function that counts how  many times the letter a is repeated in a given word
#(get the work from user as an input)

def repeat():
    word = input("enter a word: ")
    renew = list(word)
    #print(renew)
    times = renew.count('a')
    print(f"The letter a appears: {times} time(s).")

repeat()


#13) write code that counts the number of letters in a word provided by the user
#step1: ask user for input

count = "This is a tool that will count the number of letters"
print(count)

word = input("Enter in a word: ")

#step2:
length = len(word)
print(f"Your word contains {length} number of letters.")

#14) Write a function that counts down from 20
def count(num):
    num = 21
    while (num>0):
        num-=1
        print(num)

count(20)

#15) Write a function that tells if the given input is even or odd
def even_or_odd(x):
    #step1: get input from user

    """question = int(input("Enter in a number: "))"""
    #step2:
        #how to determine if a # is odd? x +1/2 = 1. Therefore if x=1, then 1+1 =2/2 ==1. X is odd.
        #a number is even if: x+1/2 !=1
            #example: 2+1=3/2 !=1 , therefore x is even.
    question = int(input("Enter in a number: "))
    x = question #Not sure how to define x

    if(x+1/2 == 1):

        print(f"the number you entered is Odd.")
    else:
        print(f"the number you entered is Even.")
even_or_odd(x)

#16) Find the length of a string given by the user as input using a counter
#variable (don't use the built-in len function)



#17) Write a loop that traverse through a string provided by the user and prints
#out one letter at a time

selection = input("Enter a phrase: ")

for i in selection:
    print(i)
