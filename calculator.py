def get_input(instream):
    return instream.read_line()

def parse_input_get_tokens(expression_str):
    tokens = []
    token = ""
    for char in expression_str:
        if char == "+":
            assert token != ""
            tokens.append(int(token))
            tokens.append("+")
            token = ""
        else:
            token+=(char)
    assert token != ""
    tokens.append(int(token))
    return tokens

def translate_tokens_to_ops(tokens):
    return (tokens[1],tokens[0],tokens[2])

def evaluate_ops(operation):
    assert operation[0] == "+"
    return operation[1]+operation[2]

class calculator(object):
    def __init__():
        return
    
    def calculate(expression_str):
        tokens = parse_input_get_tokens(expression_str)
        ops = translate_tokens_to_ops(tokens)
        return evaluate_ops(ops)

if __name__ == "main":
    calc = calculator()
    expr = sys.stdin.read_line()
    print(str(calc.calculate(expr)))
