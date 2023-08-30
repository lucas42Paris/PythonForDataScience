import sys

def check_even_odd(number):
	num = int(number)

	if num % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm Odd.")

if len(sys.argv) == 2:
	assert sys.argv[1].lstrip("-").isdigit(), "argument is not an integer"
	check_even_odd(sys.argv[1])

elif len(sys.argv) > 2:
	assert False, "more than one argument is provided"
