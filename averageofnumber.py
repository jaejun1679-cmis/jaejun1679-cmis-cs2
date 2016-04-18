import math
import time

def intro():
    print """Type any five numbers, but they must be between 0 and 9. \n """

def findevenorodd(intaverage): 
    if intaverage == int:
        evenorodd = "even"
        return evenorod
    else:
        evenorod = "odd"
        return evenorod

def output(average, intaverage, evenorod):
	return """
The average is {}.
The interger part of the average is {}. 
The interger part is {}. \n 
""".format (average, intaverage, evenorod) 

def main():
    intro()
    n1 = float(raw_input("What is the first number?: "))
    n2 = float(raw_input("What is the second number?: "))
    n3 = float(raw_input("What is the third number?: "))
    n4 = float(raw_input("What is the fourth number?: "))
    n5 = float(raw_input("What is the fifth number?: "))
    average = (n1 + n2 + n3 + n4 + n5) /5
    intaverage = int(average)
    findevenorodd(intaverage)
    print output (average, intaverage, evenorod)

main()
