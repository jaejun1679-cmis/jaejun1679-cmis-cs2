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
#We can use parameters in your function call.
# 
# 5) How do we get data out of a function call?
#The return function allows the program to spit out data back out by using return or parameters. 
#
#
#
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables q1-q20.

#a1 = 8
#a2 = 8
#a3 = -1

#b1 = 2
#b2 = 4         [x]
#b3 = 4          

#c1 = -2 
#c2 = 4
#c3 = 45         

#d1 = 8         [x]
#d2 = 6         [x]
#d3 = 2         [x]

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.


def adder(runningtotal=0, n=0):
    num = raw_input("Insert a number: ")

    if num == "":
        average = runningtotal / n
        print "The total average of the odd numbers is {}.".format(average)

    if float(num) % 2==0:
        adder()

    else:
        num = float(num)        
        n = n+1
        runningtotal += num
        adder(runningtotal, n)
        
adder()
