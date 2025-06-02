"""
grammar_classes.py contains all the classes needed to represent
a grammar text file. The classes are designed to support a
mutually recursive algorithm that can generate random sentences
from a grammar text file.
"""
import random

class Symbol:
    """
    A base class that represents a symbol in a grammar file.
    Supports derived classes TerminalSymbol and VariableSymbol.
    """

    def generate(self, grammar, rng):
        """
        A method that generates necessary data from a symbol.
        Used in TerminalSymbol and VariableSymbol.
        """
        pass

class TerminalSymbol(Symbol):
    """
    TerminalSymbol represents Terminal Symbols in a grammar file.
    """
    def __init__(self, text):
        self.text = text

    def generate(self, grammar, rng):
        """
        generate yields the text of a TerminalSymbol.

        This function is
        called by generate functions of Option classes.
        """
        yield self.text

class VariableSymbol(Symbol):
    """
    VariableSymbol represents Variable Symbols in a grammar file.
    """
    def __init__(self, name):
        self.name = name

    def generate(self, grammar, rng):
        """
        generate asks the grammar for the rule corresponding to the name of
        the VariableSymbol. Then, generate will then yield the sentence fragment
        from calling the generate function of the Rule class corresponding to the
        rule associated with this VariableSymbol.
        
        This function is called by generate functions of
        Option classes.
        """
        rule = grammar.rules[self.name]
        yield from rule.generate(grammar, rng)

class Option:
    """
    Option represents an option associated with a rule in a grammar file.
    """
    def __init__(self, weight, symbols):
        self.weight = weight
        self.symbols = symbols

    def generate(self, grammar, rng):

        """
        generate iterates through its symbols stored in its attributes, yielding
        sentence fragments from each symbol.
        """
        for symbol in self.symbols:
            yield from symbol.generate(grammar, rng)

class Rule:
    """
    Rule represents a rule in a grammar file.
    """
    def __init__(self, variable, options):
        self.variable = variable
        self.options = options

    def generate(self, grammar, rng_provider):
        """
        generate chooses one of its stored options from random using RealRandomOutcomeProvider,
        with the weights of each option influencing the chances of an option being chosen.
        The option chosen will then yield a sentence fragment.
        """
        weights = [opt.weight for opt in self.options]
        chosen = rng_provider.choices(self.options, weights)
        yield from chosen.generate(grammar, rng_provider)

class Grammar:
    """
    Grammar represents the rule structure of a grammar file by containing all the
    rules of a grammar file.
    """
    def __init__(self, rules):
        self.rules = rules

    def get_rule(self, name):
        """
        get_rule is used to extract a specific rule from a Grammar instance.
        """
        return self.rules[name]

class RealRandomOutcomeProvider:
    """
    RealRandomOutcomeProvider is a class that generates a random outcome.
    It is used by the generate function of Rule classes to select an option
    based on the weights of the different options a Rule has.

    This class is part of a test double with FakeRandomOutcomeProvider, which
    simulates 'random' outcomes instead of using the random module.
    """
    def choices(self, options, weights):
        return random.choices(options, weights=weights, k=1)[0]