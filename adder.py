import math
import time

def adder():

    value = (raw_input ("Insert a number: ")

    if value == "":
        print total
        exit()

    else:
        total += float(value)
        adder()

    print "Running total: " + float(total)

    adder()

adder()
