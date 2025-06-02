"""
testing_tools.py contains functions used to simulate main() contained in
project4.py, including functions involved in test doubles.
"""
from parse_grammar_file import parse_grammar_file
from grammar_classes import Grammar

class FakeInputProvider:
    """
    FakeInputProvider is a class meant to simulate a class that gets inputs
    from the user. It is initialized with a list of inputs.
    """
    def __init__(self, inputs):
        self._inputs = inputs

    def get_input(self):
        """
        get_input is called to return the output from popping the first value
        in the list of inputs stored in this class.
        """
        return self._inputs.pop(0)

class FakeRandomOutcomeProvider:
    """
    FakeRandomOutcomeProvider is a class involved in a test double with
    RealRandomOutcomeProvider. It is used to force fixed outcomes to occur
    by storing and returning a fixed sequence of choices.
    """
    def __init__(self, forced_choices):
        self.forced_choices = list(forced_choices)

    def choices(self, options, weights=None):
        """
        choices returns the outcome from popping the first choice in
        the list of forced_choices stored in this class.
        """
        if self.forced_choices:
            if not self.forced_choices:
                raise RuntimeError("No more forced choices available.")
            return self.forced_choices.pop(0)

def simulate_main(input_provider, rng_provider):
    """
    simulate_main is called to simulate the outcome of the main().
    simulate_main takes both FakeInputProvider and FakeRandomOutcomeProvider
    to use fixed inputs as values used for variables needed to run main() regularly.
    FakeRandomOutcomeProvider is input as the rng_provider in the for loop to
    force set outcomes to occur and print a fixed sequence of sentence fragments.
    """
    grammar_file_path = input_provider.get_input()
    sentence_count = int(input_provider.get_input())
    start_variable = input_provider.get_input()

    rules_dict = parse_grammar_file(grammar_file_path)
    grammar = Grammar(rules_dict)

    for i in range(sentence_count):
        start_rule = grammar.get_rule(start_variable)
        symbols_generator = start_rule.generate(grammar, rng_provider)
        sentence_symbols = list(symbols_generator)
        sentence = " ".join(sentence_symbols)
        print(sentence)
