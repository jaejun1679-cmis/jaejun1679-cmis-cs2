#Section 1: Terminology
# 1) What is a recursive function?
#A recursive function is a defined function that calls itself and only is completed when the requirements of the base case is met. Usually a parameter is used 
#
#
# 2) What happens if there is no base case defined in a recursive function?
#The recursive function will run for an infinite amount of times and will not be stopped.
#
#
# 3) What is the first thing to consider when designing a recursive function?
#Make sure to have a base case for the recursive function. 
#
#
# 4) How do we put data into a function call?
#Data can be put into a function call by using the raw input function. It allows the user to put in any form of data in the form of a string.
#
# 
# 5) How do we get data out of a function call?
#The return function allows the program to spit out data back out. 
#
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables q1-q20.

#a1 = 2, 2, 2, 2, 2, 2  
#a2 = 6, 6
#a3 = -1

#b1 = 2
#b2 = 1
#b3 = 16

#c1 = -2 
#c2 = 4
#c3 = 5

#d1 = 6
#d2 = 7
#d3 =

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.


def adder(runningtotal=0, n=0):
    num = float(raw_input("Insert a number: "))

    if num == "":
        runningtotal / n
        print "The total average of the odd numbers is {}.".format(float(runningtotal))

    elif (num/2) != float(num):
        n = n+1
        runningtotal += num

    adder(runningtotal)
        
adder()
