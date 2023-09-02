import sys

def filter_words_by_length(sentence, min_length):
    words = sentence.split()
    filtered_words = [word for word in words if len(word) > min_length]
    return (filtered_words)

def main():
    if len(sys.argv) != 3 or not isinstance(sys.argv[1], str) or not sys.argv[2].isdigit():
        print("Usage: python filterstring.py 'sentence' min_length")
        return
    
    try:
        sentence = sys.argv[1]
        min_length = int(sys.argv[2])

        result = filter_words_by_length(sentence, min_length)

        print(result)

    except (ValueError, IndexError):
        print("Usage: python filterstring.py 'sentence' min_length")

if __name__ == "__main__":
    main()
