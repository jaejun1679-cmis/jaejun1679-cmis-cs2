#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a) "apple" == "apple"
#b) 1 != 1
#c) 5 >= 6

#2) What does 'return' do?
#'Return' returns a value. It can be used after an calculation is 
#executed. When the python interpreter solves a math problem, you can
#"return" the value back into the interpreter so you can see (no pun
#intended).

#3) What are 2 ways indentation is important in python code?
#a) Indentation is important because it tells specific lines of code where it belongs in a certain function.
#b) And the correct indentation levels tells python when a specific function ends.

#PART 2: Reading
#Type the values for 9 of the 12 of the variables below.
#
#problem1_a) 36
#problem1_b) square root of 3
#problem1_c) square root of 0
#problem1_d) -5
#
#problem2_a) True
#problem2_b) False
#problem2_c) True
#problem2_d) False
#
#problem3_a) 0.3
#problem3_b) 0.5
#problem3_c) 0.5
#problem3_d) 0.5
#
#problem4_a) 7
#problem4_b) 5
#problem4_c) 0.125
#problem4_d) 4.5
#
#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)

def output(num1, num2, num3): #printing only if the numbers meet the given boolean expressions
    if num1 > num2 and num1 > num3:
        print """
The greatest number is {}
""".format(num1)

    elif num2 > num1 and num2 > num3:
        print """
The greatest number is {}
""".format(num2)

    elif num3 > num1 and num3 > num2:
        print """
The greatest number is {}
""".format(num3)

    elif num1 == num2 == num3:
        print """
You did not follow directions.
"""

def main():
    print "Please type in three different numbers." #simple directions givens
    num1 = float(raw_input("Number 1: ")) #raw input of user's desired numbers.
    num2 = float(raw_input("Number 2: "))
    num3 = float(raw_input("Number 3: "))
    output(num1, num2, num3)

main() #main function to execute my script
