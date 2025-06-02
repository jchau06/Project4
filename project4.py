# project4.py
#
# ICS 33 Spring 2025
# Project 4: Still Looking for Something
"""
project4.py is the file ran to run the program.
"""
from parse_grammar_file import parse_grammar_file
from grammar_classes import Grammar, RealRandomOutcomeProvider


def main() -> None:
    """
    main() is the function executes the program.
    It takes three user inputs and produces a dictionary of rules
    from the grammar text file, which is then used to create
    a Grammar object.

    Randomness in outputs is provided through RealRandomOutcomeProvider.

    Based on the integer given from sentence_count, a number
    of sentences are produced from the generators deriving from the
    Grammar object's rules, options, and symbols.
    """
    grammar_file_path = input().strip()
    sentence_count = int(input().strip())
    start_variable = input().strip()

    rules_dict = parse_grammar_file(grammar_file_path)
    grammar = Grammar(rules_dict)

    real_rng = RealRandomOutcomeProvider()

    for i in range(sentence_count):
        start_rule = grammar.get_rule(start_variable)
        symbols_generator = start_rule.generate(grammar, real_rng)
        sentence_symbols = list(symbols_generator)
        sentence = " ".join(sentence_symbols)
        print(sentence)


if __name__ == '__main__':
    main()
