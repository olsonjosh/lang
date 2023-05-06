import re


class Parser:
    def __init__(self, input_string):
        self.input_string = input_string
        self.current_token = None
        self.next_token()

    def next_token(self):
        TOKEN_REGEX = re.compile(r'^\s*("[^"]*"|\d+|[a-zA-Z_]\w*|\+|-|\*|/|\(|\)|,|;)', re.DOTALL)
        match = re.match(TOKEN_REGEX, self.input_string)
        if not match:
            self.current_token = None
        else:
            self.current_token = match.group(1)
            self.input_string = self.input_string[match.end():]

    def parse(self):
        statements = []
        while self.current_token:
            statements.append(self.parse_statement())
            if self.current_token == ';':
                self.next_token()
        return statements

    def parse_statement(self):
        if self.current_token == 'print':
            self.next_token()
            expr = self.parse_expression()
            return 'print', expr
        else:
            expr = self.parse_expression()
            return 'expr', expr

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
        if self.current_token.isdigit():
            result = int(self.current_token)
            self.next_token()
            return result
        elif self.current_token.startswith('"') and self.current_token.endswith('"'):
            result = self.current_token[1:-1]
            self.next_token()
            return result
        elif self.current_token == '(':
            self.next_token()
            result = self.parse_expression()
            if self.current_token != ')':
                raise SyntaxError('Expected )')
            self.next_token()
            return result
        else:
            raise SyntaxError('Expected number, string, or (')
