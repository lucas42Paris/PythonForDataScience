def NULL_not_found(object: any) -> int:
	if object is None:
		print("Nothing: None <class 'NoneType'>")

	elif object is False:
		print("Fake: False <class 'bool'>")
	
	elif isinstance(object, float):
		print("Cheese: nan <class 'float'>")

	elif isinstance(object, int):
		print("Zero: 0 <class 'int'>")

	elif object == "":
		print("Empty: <class 'str'>")

	else:
		print("Type not Found")
		return (1)

	return (0)
