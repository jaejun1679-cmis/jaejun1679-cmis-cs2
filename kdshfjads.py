import math

def function(arg):
    if arg == int(arg):
        return True
    else:
        return False
problem2_a = function(15)
problem2_b = function(math.pi)
problem2_c = function("25")
problem2_d = function(True)

print problem2_a
print problem2_b
print problem2_c
print problem2_d

def function4(a, b, c):
    result = a + b + c
    if a > b and b > c:
        result = result - c
    elif a < b or b < c:
        result = result - a

    if not (result > a * b * c):
        result = a * b * c
	
    return result

problem4_a = function4(2, 3, 4)
problem4_b = function4(3, 2, 1)
problem4_c = function4(0.5, 0.5, 0.5)
problem4_d = function4(3, 2, 0.5)

print problem4_a
print problem4_b
print problem4_c
print problem4_d
