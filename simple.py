def sub(a, b):
	c = a - b
	return c

def output(name, a, b, c):
	return """
Hello {}!
Did you know: 
{} - {} = {}
""".format(name, a, b, c)

def main():
	'
	name = raw_input("What is your name?: ")
	a = raw_input("Tell me a number?: ")
	b = raw_input("Tell me another number: ")
	c = sub(int(a), int(b)) 
	print output(name, a, b, c)
main()
