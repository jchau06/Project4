from grammar_classes import VariableSymbol, TerminalSymbol, Option, Rule

def parse_grammar_file(path):
    rules = {}
    with open(path, "r") as f:
        lines = [line.strip() for line in f]

    i = 0
    while i < len(lines):
        if lines[i] == '{':
            var_name = lines[i + 1]
            i += 2
            options = []

            while lines[i] != '}':
                weight_str, *symbols_str = lines[i].split()
                weight = int(weight_str)
                symbols = [
                    VariableSymbol(symbol[1:-1]) if symbol.startswith("[") and symbol.endswith("]")
                    else TerminalSymbol(symbol) for symbol in symbols_str
                ]
                options.append(Option(weight, symbols))
                i += 1
            rules[var_name] = Rule(var_name, options)
        i += 1
    return rules