import re


class Parser:
    def __init__(self, input_string):
        self.input_string = input_string
        self.current_token = None
        self.next_token()

    def next_token(self):
        match = re.match(r'^\s*(\d+|\+|-|\*|/|\(|\))', self.input_string)
        if not match:
            self.current_token = None
        else:
            self.current_token = match.group(1)
            self.input_string = self.input_string[match.end():]

    def parse(self):
        result = self.parse_expression()
        if self.current_token:
            raise SyntaxError('Unexpected token: ' + self.current_token)
        return result

    def parse_expression(self):
        result = self.parse_term()
        while self.current_token in ('+', '-'):
            operator = self.current_token
            self.next_token()
            term = self.parse_term()
            if operator == '+':
                result += term
            else:
                result -= term
        return result

    def parse_term(self):
        result = self.parse_factor()
        while self.current_token in ('*', '/'):
            operator = self.current_token
            self.next_token()
            factor = self.parse_factor()
            if operator == '*':
                result *= factor
            else:
                result /= factor
        return result

    def parse_factor(self):
        if self.current_token == '(':
            self.next_token()
            result = self.parse_expression()
            if self.current_token != ')':
                raise SyntaxError('Expected )')
            self.next_token()
        elif self.current_token.isdigit():
            result = int(self.current_token)
            self.next_token()
        else:
            raise SyntaxError('Expected number or (')
        return result
