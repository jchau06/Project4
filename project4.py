# project4.py
#
# ICS 33 Spring 2025
# Project 4: Still Looking for Something
from read_file import parse_grammar_file


def main() -> None:
    path = input()
    grammar = parse_grammar_file(path)

    print(grammar)

    for rule, options in grammar.items():
        print(f"Rule: {rule}")
        for weight, symbols in options:
            print(f"  Weight: {weight}, Symbols: {symbols}")


if __name__ == '__main__':
    main()


