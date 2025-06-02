
import unittest

class FakeInputProvider:
    def __int__(self, inputs):
        self._inputs = list(inputs)

    def get_input(self):
        return self._inputs.pop(0)

class FakeRandomOutcomeProvider:
    def __init__(self, forced_choices):
        self.forced_choices = list(forced_choices)

    def choose_weighted(self, weighted_options):
        if self.forced_choices:
            return self.forced_choices.pop(0)
        else:
            return weighted_options[0][1]