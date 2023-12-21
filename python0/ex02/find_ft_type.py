def all_thing_is_obj(object: any) -> int:
    if isinstance(object, list):
        print(f"List : <class '{type(object).__name__}'>")
    elif isinstance(object, tuple):
        print(f"Tuple : <class '{type(object).__name__}'>")
    elif isinstance(object, set):
        print(f"Set : <class '{type(object).__name__}'>")
    elif isinstance(object, dict):
        print(f"Dict : <class '{type(object).__name__}'>")
    elif isinstance(object, str):
        print(object, f"is in the kitchen : <class '{type(object).__name__}'>")
    else:
        print("Type not found")

    return (42)
