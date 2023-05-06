import sys
from parser import Parser


def main():
    input_string = '3 + 4 * (2 - 1) / 5'
    parser = Parser(input_string)
    result = parser.parse()
    print(f'{input_string} = {result}')


if __name__ == '__main__':
    sys.exit(main())
