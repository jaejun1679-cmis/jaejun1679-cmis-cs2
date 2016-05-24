import time

def countdown(x):
    while x >= 0:
        print x
        time.sleep(0.5)
        x -= 1
    
def countup(x):
    while x <= 10:
        print x
        time.sleep(0.5)
        x += 1

countdown(10)
countup(0)
