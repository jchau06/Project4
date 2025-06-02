"""
test_grammar_file_execution takes testing_tools to simulate the processing
and execution of temporary grammar files through using functions from
testing_tools. This test suite contains tests that simulate the behavior of
main() and verifies behavior relating to sentence count, start variables, and
correct output.

This test suite additionally tests the behavior of grammar_classes and verifies
that the mutually recursive algorithm is working correctly.
"""

import unittest
import tempfile
import contextlib
import io
from testing_tools import *


class TestGrammarFileExecution(unittest.TestCase):
    def test_number_of_printed_statements_matches_sentence_count(self):
        with tempfile.NamedTemporaryFile(mode = 'w', delete_on_close = False) as my_temp_file:
            my_temp_file.write('{\n')
            my_temp_file.write('HowIsBoo\n')
            my_temp_file.write('1 Boo is [Adjective] today\n')
            my_temp_file.write('}\n')
            my_temp_file.write('\n')
            my_temp_file.write('{\n')
            my_temp_file.write('Adjective\n')
            my_temp_file.write('1 happy\n')
            my_temp_file.write('}\n')
            my_temp_file.close()

            fake_inputs = [my_temp_file.name, "3", "HowIsBoo"]
            fake_input_provider = FakeInputProvider(fake_inputs)

            rules_dict = parse_grammar_file(my_temp_file.name)
            grammar = Grammar(rules_dict)

            how_is_boo_opt = grammar.get_rule("HowIsBoo").options[0]
            adjective_opt = grammar.get_rule("Adjective").options[0]
            forced_options = [
                how_is_boo_opt, adjective_opt,
                how_is_boo_opt, adjective_opt,
                how_is_boo_opt, adjective_opt
            ]

            fake_rng_provider = FakeRandomOutcomeProvider(forced_options)

            with contextlib.redirect_stdout(io.StringIO()) as output:
                simulate_main(fake_input_provider, fake_rng_provider)

            self.assertEqual(output.getvalue(),
                             "Boo is happy today\nBoo is happy today\nBoo is happy today\n")

    def test_different_outputs_from_different_start_variables(self):
        with tempfile.NamedTemporaryFile(mode = 'w', delete_on_close = False) as my_temp_file:
            my_temp_file.write('{\n')
            my_temp_file.write('HowIsBoo\n')
            my_temp_file.write('1 Boo is [Adjective] today\n')
            my_temp_file.write('}\n')
            my_temp_file.write('\n')
            my_temp_file.write('{\n')
            my_temp_file.write('HowIsChancy\n')
            my_temp_file.write('1 Chancy is [Adjective] today\n')
            my_temp_file.write('}\n')
            my_temp_file.write('\n')
            my_temp_file.write('{\n')
            my_temp_file.write('Adjective\n')
            my_temp_file.write('1 happy\n')
            my_temp_file.write('}\n')
            my_temp_file.close()

            fake_inputs = [my_temp_file.name, "1", "HowIsBoo"]
            fake_input_provider = FakeInputProvider(fake_inputs)

            rules_dict = parse_grammar_file(my_temp_file.name)
            grammar = Grammar(rules_dict)

            how_is_boo_opt = grammar.get_rule("HowIsBoo").options[0]
            adjective_opt = grammar.get_rule("Adjective").options[0]
            forced_options = [
                how_is_boo_opt, adjective_opt,
            ]

            fake_rng_provider = FakeRandomOutcomeProvider(forced_options)

            with contextlib.redirect_stdout(io.StringIO()) as output:
                simulate_main(fake_input_provider, fake_rng_provider)

            self.assertEqual(output.getvalue(),
                             "Boo is happy today\n")

            fake_inputs = [my_temp_file.name, "1", "HowIsChancy"]
            fake_input_provider = FakeInputProvider(fake_inputs)

            rules_dict = parse_grammar_file(my_temp_file.name)
            grammar = Grammar(rules_dict)

            how_is_boo_opt = grammar.get_rule("HowIsChancy").options[0]
            adjective_opt = grammar.get_rule("Adjective").options[0]
            forced_options = [
                how_is_boo_opt, adjective_opt,
            ]

            fake_rng_provider = FakeRandomOutcomeProvider(forced_options)

            with contextlib.redirect_stdout(io.StringIO()) as second_output:
                simulate_main(fake_input_provider, fake_rng_provider)

            self.assertEqual(second_output.getvalue(),
                             "Chancy is happy today\n")

    def test_generating_correct_output_with_fake_rng(self):
        with tempfile.NamedTemporaryFile(mode = 'w', delete_on_close = False) as my_temp_file:
            my_temp_file.write('{\n')
            my_temp_file.write('HowIsBoo\n')
            my_temp_file.write('1 Boo is [Adjective] today\n')
            my_temp_file.write('}\n')
            my_temp_file.write('\n')
            my_temp_file.write('{\n')
            my_temp_file.write('Adjective\n')
            my_temp_file.write('3 happy\n')
            my_temp_file.write('3 perfect\n')
            my_temp_file.write('1 relaxing\n')
            my_temp_file.write('1 fulfilled\n')
            my_temp_file.write('2 excited\n')
            my_temp_file.write('}\n')
            my_temp_file.close()

            fake_inputs = [my_temp_file.name, "5", "HowIsBoo"]
            fake_input_provider = FakeInputProvider(fake_inputs)

            rules_dict = parse_grammar_file(my_temp_file.name)
            grammar = Grammar(rules_dict)

            how_is_boo_opt = grammar.get_rule("HowIsBoo").options[0]
            happy_opt = grammar.get_rule("Adjective").options[0]
            perfect_opt = grammar.get_rule("Adjective").options[1]
            relaxing_opt = grammar.get_rule("Adjective").options[2]
            fulfilled_opt = grammar.get_rule("Adjective").options[3]
            excited_opt = grammar.get_rule("Adjective").options[4]
            forced_options = [
                how_is_boo_opt, happy_opt,
                how_is_boo_opt, perfect_opt,
                how_is_boo_opt, relaxing_opt,
                how_is_boo_opt, fulfilled_opt,
                how_is_boo_opt, excited_opt
            ]

            fake_rng_provider = FakeRandomOutcomeProvider(forced_options)

            with contextlib.redirect_stdout(io.StringIO()) as output:
                simulate_main(fake_input_provider, fake_rng_provider)

            self.assertEqual(output.getvalue(),
                             "Boo is happy today\nBoo is perfect today\nBoo is relaxing today\nBoo is fulfilled today\nBoo is excited today\n")


