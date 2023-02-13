import sys

from kg.db.generate_words import generate


def print_all(words):
    for word in words:
        print(word)


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            print_all(generate(sys.argv[1]))
        else:
            print_all(generate())
    except Exception as e:
        print(f"Ката: {repr(e)}")
