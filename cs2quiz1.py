#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
#The "=" symbol is called an assignment operator and it does what it says. 
#It assigns values to variables, which is called an assignment statement.
#ex: x = 5

#2 3pts) Write a technical definition for 'function'
#A function is a defined set of sequences which consists of statements that performs a computation.
#Think of a function like a vending machine. 
#Some input goes in (the coins), buttons are pressed (computation), and then the drink or food comes out (output). 

#3 1pt) What does the keyword "return" do?
#"Return" returns a value. It is used at the end of function in order for the funtion to "spit" some value back out. 

#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1: String: "hi", "bye", str(5)
#	2: Intergers: 5, 6, 7, 8
#	3: Float: 5.0, 3.14, 0.8946
#	4: Boolean: True & False
#	5: Tuple: "JJC", "is so cool", "42"

#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
#Defining a function is a header in a function. It defines the function name.  
#ex: defa(b):
#Calling a function executes the function. It runs the set of codes.  
#ex: a(5)

#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1: Input: The user gives the function some data. It can be through a variable or even using the function (raw_input).
#	2: Calculation/ Computation: This is the main body of the function. The function will do whatever the coding says to do. 
#	3: Output: The output is the value once the computation has been completed. This can be a sum of any numbers or even a sentence refering to how cute cats can be.
#(Refer to the vending machine analogy above. Thank you.) 
#
#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

import math
def output(ac1, ac2, ac3, dc1, dc2, dc3, td):
	return """

You have insert the values: {}, {}, and {} as the areas of the three circle we will be using! 
This means that the diamters will be....hmmmm....


The diameter of the first circle is {}.
The diameter of the second circle is {}.
The diameter of the thrid circle is {}.

The total of the diameters of the first circle, second cricle and the thrid circle is {}.
""".format(ac1, ac2, ac3, dc1, dc2, dc3, td)

def main():
    print "Welcome to JJC's Magical Area to Diameter Calculator! \nNow lets begin!" 
    ac1 = float(raw_input("Please insert an area of a circle: "))
    ac2 = float(raw_input(""""Another one" - DJ Khaled : """))
    ac3 = float(raw_input("Now type some random number between 5 and 500: "))
    dc1 = 2 * (math.sqrt((ac1/math.pi)))
    dc2 = 2 * (math.sqrt((ac2/math.pi)))
    dc3 = 2 * (math.sqrt((ac3/math.pi)))
    td = dc1 + dc2 + dc3
    print output(ac1, ac2, ac3, dc1, dc2, dc3, td)

main()



