import math
import time

def intro():
    print """Type any five numbers, but they must be between 0 and 9. \n """

def findevenorodd(intaverage):
    if (intaverage/2) == int:
        evenorodd = "even"
        return evenorodd
    else:
        evenorodd = "odd"
        return evenorodd

def output(average, intaverage, evenorodd):
	return """
The average is {}.
The interger part of the average is {}. 
The interger part is {}. \n 
""".format (average, intaverage, evenorodd)

def rangefind(n1, n2, n3, n4, n5):
    if n1 >= 0 and n1 < 10:
        rangefind(n2)
        if not:
            print "Out of range."
            exit()

    if n2 >= 0 and n2 < 10:
        rangefind(n3)
        if not:
            print "Out of range."
            exit()

    if n3 >= 0 and n3 < 10:
        rangefind(n4)
        if not:
            print "Out of range."
            exit()

    if n4 >= 0 and n4 < 10:
        rangefind(n5)
        if not:
            print "Out of range."
            exit()

    if not n5 >= 0 and n5 < 10:
        print "Out of range."
        exit()

def main():
    intro()
    n1 = float(raw_input("What is the first number?: "))
    n2 = float(raw_input("What is the second number?: "))
    n3 = float(raw_input("What is the third number?: "))
    n4 = float(raw_input("What is the fourth number?: "))
    n5 = float(raw_input("What is the fifth number?: "))
    rangefind(n1, n2, n3, n4, n5)
    average = (n1 + n2 + n3 + n4 + n5) /5
    intaverage = int(average)
    evenorodd = findevenorodd(intaverage)
    print output (average, intaverage, evenorodd)

main()
