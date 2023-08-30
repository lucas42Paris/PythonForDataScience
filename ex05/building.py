import sys

def count_characters(text):
    """
    Count the number of upper-case, lower-case, punctuation,
    digits, and spaces in the given text.
    """
    upper_count = 0
    lower_count = 0
    punctuation_count = 0
    digit_count = 0
    space_count = 0

    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char.isspace():
            space_count += 1
        elif char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
            punctuation_count += 1

    return (upper_count, lower_count, punctuation_count, digit_count, space_count)

def main():
    """
    Main function to handle user input and display results.
    """
    if len(sys.argv) == 1:
        text = input("What is the text to count?\n")
    elif len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        raise AssertionError("more than one argument is provided.")

    upper_count, lower_count, punctuation_count, digit_count, space_count = count_characters(text)
    total_count = len(text)

    print(f"The text contains {total_count} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")

if __name__ == "__main__":
    main()
