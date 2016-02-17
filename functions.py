import math #imported the module so that math functions can be executed 
def add(a, b): #defined a function
	return (a+b) #told what the value the function should return; hence the name
add(3, 4) #called the function

def sub(a, b): 
	return (a-b)
sub(5, 3)

def mul(a, b):
	return (a*b)
mul(4, 4)

def div(a, b):
	return (a/b)
div(2, 3)

def hours_from_seconds(a):
    return (a/3600)
hours_from_seconds(86400)

def circle_area(a):
	return (math.pi*(a**2))
circle_area(5)

def sphere_volume(a):
    b = float(4/3)
    return ((b)*math.pi*(a**3))
sphere_volume(5)

def avg_volume(a, b):
    c = float(a/2)
    d = float(b/2)
    z = float(4/3)
    return (((z)*math.pi*(c**3)) + ((z)*math.pi*(d**3)))/2
avg_volume(10 ,20)

def area_tri(a, b, c):
    s = (a + b + c)/2
    return float(math.sqrt((s(s-a)(s-b)(s-c))))

def right_align(a):
    print (" "*80 - len(a))

def msg_box(txt):
	    return "+" + ((len(txt)+4)*"-") + "+" + "\n" + "|" + (2*" ") + (txt)+ (2*" ") + "|" + "\n" + "+" + ((len(txt)+4)*"-") + "+"



