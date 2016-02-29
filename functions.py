import math #imported the module so that math functions can be executed 

def msg_box(txt):
	return "+" + ((len(txt)+4)*"-") + "+" + "\n" + "|" + (2*" ") + (txt)+ (2*" ") + "|" + "\n" + "+" + ((len(txt)+4)*"-") + "+"

def add(a, b): #defined a function
	return (a+b) #told what the value the function should return; hence the name
added = add(3, 4) #called the function and stored the results in a variable 
print  msg_box(str(added))

def sub(a, b): 
	return (a-b)
subbed = sub(5, 3)
print  msg_box(str(subbed))

def mul(a, b):
	return (a*b)
multi = mul(4, 4)
print  msg_box(str(multi))

def div(a, b):
	return float(a)/b
divid = div(2, 3)
print  msg_box(str(divid))

def hours_from_seconds(a):
    return (a/3600)
hts = hours_from_seconds(86400)
print  msg_box(str(hts))

def circle_area(a):
	return (math.pi*(a**2))
cA = circle_area(5)
print  msg_box(str(cA))

def sphere_volume(a): #fix calculations
    b = float(4)/3
    return b*math.pi*a**3
sV = sphere_volume(5)
print  msg_box(str(sV))

def avg_volume(a, b):
    c = float(a)/2
    d = float(b)/2
    z = float(4)/3
    return (((z)*math.pi*(c**3)) + ((z)*math.pi*(d**3)))/2
avgV = avg_volume(10 ,20)
print  msg_box(str(avgV))

def area_tri(a, b, c):	
    s = (a + b + c)/2
    return float(math.sqrt((s*(s-a)*(s-b)*(s-c))))
triA = area_tri(1, 2, 2.5)
print  msg_box(str(triA))

def right_align(a):
	return (80 - len(a)) * " " + a
rightaltxt = right_align("Hello World!")
print  msg_box(str(rightaltxt))

def center_txt(a):
	return (40 - len(a)) * " " + a
centertxt = center_txt("Hello World!")
print  msg_box(str(centertxt))

output = "Here are some pretty cool numbers. I don't even know why but here they are: " + str(added) + str(subbed) + str(multi) + str(divid) + ". Thats right. " + str(added) + "is a cool number. " + str(subbed) + "That number. is pretty cool too. Ever wondered how many seconds are in a day? Well there are" + str(hts) + "hours and in seconds that would be 86400. If there was a circle, a random circle, and it had a radius of 5 units, the area would be" + str(cA) + ". Now think if another randomized sphere. For no apparent reason, it also should have a radius of 5 units. The volume now would be " + str(sV) + ". If you had two sphere now with the radii of 10 and 20 units, the average of their volumes would be " + str(avgV) + ".   
