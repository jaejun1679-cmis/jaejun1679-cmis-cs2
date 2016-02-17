def output(name, h2, w2, bmi):
	return """
Hello {}!
Your current BMI is: {} kg/m^2
""".format(name, bmi)

def main():
	name = raw_input("What is your name?: ")
	h1 = raw_input("What is you height? (meters only): ")
	w1 = raw_input("What is your weight? (kilograms only): ")
	h2 = float(h1)
	w2 = float(w1)
	bmi = w2 / (h2**2)
	print output(name, h2, w2, bmi)

main()
