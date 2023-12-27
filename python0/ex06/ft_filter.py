# print(filter.__doc__)

def ft_filter(function, iterable):
	return (item for item in iterable if function(item))

def main():
	numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	even_numbers = ft_filter(lambda x: x % 2 == 0, numbers)
	print(list(even_numbers))

if __name__ == "__main__":
	main()
