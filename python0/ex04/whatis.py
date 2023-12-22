import sys

if len(sys.argv[1:]) == 0:
    sys.exit()

assert len(sys.argv[1:]) == 1, "more than one argument is provided"

try:
    number = int(sys.argv[1])
except ValueError:
    raise AssertionError("argument is not an integer")

if number % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
