import math
import time

def adder(runningtotal=0):
    value =raw_input("Insert a number: ")
    if value == "":
        print "The total sum of the numbers is {}.".format(runningtotal)
	exit()
    else:
	print "The current total sum of the numbers is {}.".format(runningtotal)
        adder(runningtotal)
    runningtotal += float(value)

adder()
