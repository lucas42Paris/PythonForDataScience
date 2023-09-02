import sys

NESTED_MORSE = {
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
    " ": "/ ",
}

def encode_to_morse(text):
    morse_message = ""

    for char in text:
        if char.upper() in NESTED_MORSE:
            morse_message += NESTED_MORSE[char.upper()]
        else:
            raise AssertionError("Invalid character in input: " + char)

    return (morse_message)

def main():
    if len(sys.argv) != 2 or not isinstance(sys.argv[1], str):
        print("Usage: python sos.py 'message'")
        return

    try:
        input_text = sys.argv[1]
        morse_result = encode_to_morse(input_text)
        print(morse_result)

    except AssertionError as e:
        print(e)

if __name__ == "__main__":
    main()
