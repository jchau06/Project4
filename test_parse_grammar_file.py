import tempfile
import unittest
from pathlib import Path
from parse_grammar_file import parse_grammar_file
from grammar_classes import Grammar, Rule, Option, TerminalSymbol, VariableSymbol

class TestParseGrammarFile(unittest.TestCase):
    def test_parsing_output_does_not_include_comments(self):
        with tempfile.NamedTemporaryFile(mode = 'w', delete_on_close = False) as my_temp_file:
            my_temp_file.write('# This is a comment.\n')
            my_temp_file.close()

            with open(my_temp_file.name, mode = 'r') as file:
                temp_path = Path(file.name)
                grammar = parse_grammar_file(temp_path)
                self.assertEqual(grammar, {})

    def test_parser_returns_grammar_verify_attributes(self):
        with tempfile.NamedTemporaryFile(mode = 'w', delete_on_close = False) as my_temp_file:
            my_temp_file.write('{\n')
            my_temp_file.write('HowIsBoo\n')
            my_temp_file.write('1 Boo is [Adjective] today\n')
            my_temp_file.write('}\n')
            my_temp_file.close()

            with open(my_temp_file.name, mode = 'r') as file:
                temp_path = Path(file.name)
                rules_dict = parse_grammar_file(temp_path)
                grammar = Grammar(rules_dict)
                self.assertEqual(len(grammar.rules), 1)
                self.assertEqual(grammar.rules['HowIsBoo'].variable, 'HowIsBoo')
                self.assertEqual(grammar.rules['HowIsBoo'].options[0].weight, 1)
                self.assertEqual(grammar.rules['HowIsBoo'].options[0].symbols[0].text, 'Boo')
                self.assertEqual(grammar.rules['HowIsBoo'].options[0].symbols[1].text, 'is')
                self.assertEqual(grammar.rules['HowIsBoo'].options[0].symbols[2].name, 'Adjective')
                self.assertEqual(grammar.rules['HowIsBoo'].options[0].symbols[3].text, 'today')

    def test_parser_returns_grammar_verify_instances(self):
        with tempfile.NamedTemporaryFile(mode = 'w', delete_on_close = False) as my_temp_file:
            my_temp_file.write('{\n')
            my_temp_file.write('HowIsBoo\n')
            my_temp_file.write('1 Boo is [Adjective] today\n')
            my_temp_file.write('}\n')
            my_temp_file.close()

            with open(my_temp_file.name, mode = 'r') as file:
                temp_path = Path(file.name)
                rules_dict = parse_grammar_file(temp_path)
                grammar = Grammar(rules_dict)
                self.assertIsInstance(grammar, Grammar)
                self.assertIsInstance(grammar.rules['HowIsBoo'], Rule)
                self.assertIsInstance(grammar.rules['HowIsBoo'].options[0], Option)
                self.assertIsInstance(grammar.rules['HowIsBoo'].options[0].symbols[0],
                                      TerminalSymbol)
                self.assertIsInstance(grammar.rules['HowIsBoo'].options[0].symbols[2],
                                      VariableSymbol)

    def test_parser_returns_grammar_with_multiple_rules_with_multiple_options(self):
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

            with open(my_temp_file.name, mode = 'r') as file:
                temp_path = Path(file.name)
                rules_dict = parse_grammar_file(temp_path)
                grammar = Grammar(rules_dict)
                self.assertEqual(len(grammar.rules), 2)
                self.assertEqual(len(grammar.rules['HowIsBoo'].options), 1)
                self.assertEqual(len(grammar.rules['Adjective'].options), 5)