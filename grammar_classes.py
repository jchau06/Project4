import random

class Symbol:
    def generate(self, grammar):
        pass

class TerminalSymbol(Symbol):
    def __init__(self, text):
        self.text = text

    def generate(self, grammar):
        yield self.text

class VariableSymbol(Symbol):
    def __init__(self, name):
        self.name = name

    def generate(self, grammar):
        rule = grammar.rules[self.name]
        yield from rule.generate(grammar)

class Option:
    def __init__(self, weight, symbols):
        self.weight = weight
        self.symbols = symbols

    def generate(self, grammar):
        for symbol in self.symbols:
            yield from symbol.generate(grammar)

class Rule:
    def __init__(self, variable, options):
        self.variable = variable
        self.options = options

    def generate(self, grammar):
        weights = [opt.weight for opt in self.options]
        chosen = random.choices(self.options, weights = weights, k = 1)[0]
        yield from chosen.generate(grammar)

class Grammar:
    def __init__(self, rules):
        self.rules = rules

    def get_rule(self, name):
        return self.rules[name]