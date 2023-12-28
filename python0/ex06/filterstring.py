import sys

def main():
    assert len(sys.argv) == 3 and isinstance(sys.argv[1], str) and sys.argv[2].isdigit(), "the arguments are bad"

    input_string = sys.argv[1]
    min_length = int(sys.argv[2])

    filtered_words = filter(lambda word: len(word) > min_length, input_string.split())

    print(list(filtered_words))

if __name__ == "__main__":
    main()
