import sys

def encode_morse(text):
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ",
        "E": ". ", "F": "..-. ", "G": "--. ", "H": ".... ",
        "I": ".. ", "J": ".--- ", "K": "-.- ", "L": ".-.. ",
        "M": "-- ", "N": "-. ", "O": "--- ", "P": ".--. ",
        "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
        "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ",
        "Y": "-.-- ", "Z": "--.. ",
        "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ",
        "4": "....- ", "5": "..... ", "6": "-.... ", "7": "--... ",
        "8": "---.. ", "9": "----. "
    }

    text = text.upper()

    try:
        morse_code = ''.join(NESTED_MORSE[char] for char in text)
    except KeyError:
        raise AssertionError("the arguments are bad")

    return (morse_code)

def main():
    assert len(sys.argv) == 2 and isinstance(sys.argv[1], str), "the arguments are bad"

    print(encode_morse(sys.argv[1]).strip())

if __name__ == "__main__":
    main()
