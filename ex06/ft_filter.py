def ft_filter(function, iterable):
	return (x for x in iterable if function(x))

def main():
	numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

	result = list(ft_filter(lambda x: x % 2 == 0, numbers_list))

	print(result)

if __name__ == "__main__":
	main()
