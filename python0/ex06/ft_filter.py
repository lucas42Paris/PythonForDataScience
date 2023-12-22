# print(filter.__doc__)

# filter(function or None, iterable)

def is_odd(n):
    return (n % 2 == 0)

nbr = [1, 2, 3, 4, 5, 6]

result = filter(is_odd, nbr)
odd_nbr = list(result)

print(odd_nbr)
