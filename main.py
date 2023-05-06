import sys
from parser import Parser


def main():
    input_string = 'print "hello, world!"\n3 + 4 * (2 - 1) / 5\n'
    parser = Parser(input_string)
    statements = parser.parse()
    for statement in statements:
        if statement[0] == 'print':
            print(statement[1])
        else:
            print(statement[1], end=' ')


if __name__ == '__main__':
    sys.exit(main())
