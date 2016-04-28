import math
import time

def adder():

    value = (raw_input ("Insert a number: ")

    if value == " ":
        print "Running total: " + str(total)
        exit()

    else:
        total += float(value)
        continue

    adder()

adder()
