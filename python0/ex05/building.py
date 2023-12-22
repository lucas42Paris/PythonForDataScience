import sys
import string

def text_analysis(str):
    count_characters = len(str)
    count_upper = sum(1 for char in str if char.isupper())
    count_lower = sum(1 for char in str if char.islower())
    count_punct = sum(1 for char in str if char in string.punctuation)
    count_spaces = sum(1 for char in str if char.isspace())
    count_digits = sum(1 for char in str if char.isdigit())

    print(f"The text contains {count_characters} characters:")
    print(f"{count_upper} upper letters")
    print(f"{count_lower} lower letters")
    print(f"{count_punct} punctuation marks")
    print(f"{count_spaces} spaces")
    print(f"{count_digits} digits")

def main():
    if len(sys.argv[1:]) == 0:
        # print("Usage: python building.py <string>")
        sys.exit(1)

    assert len(sys.argv[1:]) == 1, "more than one argument is provided"

    text_analysis(sys.argv[1])

if __name__ == "__main__":
    main()
