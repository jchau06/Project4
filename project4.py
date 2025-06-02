# project4.py
#
# ICS 33 Spring 2025
# Project 4: Still Looking for Something
from parse_grammar_file import parse_grammar_file
from grammar_classes import Grammar


def main() -> None:
    grammar_file_path = input().strip()
    sentence_count = int(input().strip())
    start_variable = input().strip()

    rules_dict = parse_grammar_file(grammar_file_path)
    grammar = Grammar(rules_dict)


    for i in range(sentence_count):
        start_rule = grammar.get_rule(start_variable)

        symbols_generator = start_rule.generate(grammar)

        sentence_symbols = list(symbols_generator)

        sentence = " ".join(sentence_symbols)

        print(sentence)


if __name__ == '__main__':
    main()
