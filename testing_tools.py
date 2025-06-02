from parse_grammar_file import parse_grammar_file
from grammar_classes import Grammar

class FakeInputProvider:
    def __int__(self, inputs):
        self._inputs = list(inputs)

    def get_input(self):
        return self._inputs.pop(0)

class FakeRandomOutcomeProvider:
    def __init__(self, forced_choices):
        self.forced_choices = list(forced_choices)

    def choices(self, options, weights):
        if self.forced_choices:
            return self.forced_choices.pop(0)
        else:
            return options[0]

def simulate_main(input_provider, rng_provider):
    grammar_file_path = input_provider.get_input()
    sentence_count = input_provider.get_input()
    start_variable = input_provider.get_input()

    rules_dict = parse_grammar_file(grammar_file_path)
    grammar = Grammar(rules_dict)

    fake_rng = rng_provider

    for i in range(sentence_count):
        start_rule = grammar.get_rule(start_variable)
        symbols_generator = start_rule.generate(grammar, fake_rng)
        sentence_symbols = list(symbols_generator)
        sentence = " ".join(sentence_symbols)
        print(sentence)
