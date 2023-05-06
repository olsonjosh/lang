import sys
from parser import Parser


def main():
    input_string = '2 + 3 * 4'
    parser = Parser(input_string)
    expr = parser.parse_expression()
    cpp_code = f"std::cout << {expr};"
    print(cpp_code)


if __name__ == '__main__':
    sys.exit(main())
