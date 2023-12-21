def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} <class '{type(object).__name__}'>")
    elif isinstance(object, float) and str(object) == "nan":
        print(f"Cheese: {object} <class '{type(object).__name__}'>")
    elif object is False:
        print(f"Fake: {object} <class '{type(object).__name__}'>")
    elif object == 0:
        print(f"Zero: {object} <class '{type(object).__name__}'>")
    elif object == '':
        print(f"Empty: <class '{type(object).__name__}'>")
    else:
        print("Type not Found")
        return 1

    return 0
