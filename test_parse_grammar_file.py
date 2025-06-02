import tempfile
import unittest
from pathlib import Path
from parse_grammar_file import parse_grammar_file

class TestParseGrammarFile(unittest.TestCase):
    def test_parsing_output_does_not_include_comments(self):
        with tempfile.NamedTemporaryFile(mode = 'w', delete_on_close = False) as my_temp_file:
            my_temp_file.write('# This is a comment.\n')
            my_temp_file.close()

            with open(my_temp_file.name, mode = 'r') as file:
                temp_path = Path(file.name)
                grammar = parse_grammar_file(temp_path)
                self.assertEqual(grammar, {})

    def test_parser_returns_rule_with_one_option(self):
        with tempfile.NamedTemporaryFile(mode = 'w', delete_on_close = False) as my_temp_file:
            my_temp_file.write('{\n')
            my_temp_file.write('HowIsBoo\n')
            my_temp_file.write('1 Boo is [Adjective] today\n')
            my_temp_file.write('}\n')
            my_temp_file.close()

            with open(my_temp_file.name, mode = 'r') as file:
                temp_path = Path(file.name)
                grammar = parse_grammar_file(temp_path)
                self.assertEqual(len(grammar), 1)
                self.assertEqual(grammar['HowIsBoo'], [(1, ['Boo', 'is', '[Adjective]', 'today'])])

    def test_parser_returns__multiple_rules_with_multiple_options(self):
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
                grammar = parse_grammar_file(temp_path)
                self.assertEqual(len(grammar), 2)
                self.assertEqual(grammar['HowIsBoo'], [(1, ['Boo', 'is', '[Adjective]', 'today'])])
                self.assertEqual(grammar['Adjective'], [(3, ['happy']), (3, ['perfect']), (1, ['relaxing']), (1, ['fulfilled']), (2, ['excited'])])
