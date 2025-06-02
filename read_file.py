
from pathlib import Path

def parse_grammar_file(path):
    grammar = {}
    with open(path, "r") as f:
        lines = [line.strip() for line in f]

    i = 0
    while i < len(lines):
        if lines[i] == '{':
            i += 1
            rule_name = lines[i]
            i += 1
            options = []

            while lines[i] != '}':
                parts = lines[i].split()
                weight = int(parts[0])
                symbols = parts[1:]
                options.append((weight, symbols))
                i += 1

            grammar[rule_name] = options
        i+= 1

    return grammar