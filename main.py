import subprocess
import sys

from parser import Parser


def main():
    input_string = '2 + 3 * 4;'
    parser = Parser(input_string)
    statements = parser.parse()
    cpp_code = ''.join(f"std::cout << {expr};\n" for _, expr in statements)
    print(f'Code: \n{cpp_code}\nOutput:')

    with open('output.cpp', 'w') as f:
        f.write(f'#include <iostream>\n\nint main() {{\n{cpp_code}}}')

    subprocess.run(['clang++', '-std=c++20', '-o', 'output', 'output.cpp'])
    subprocess.run(['./output'])


if __name__ == '__main__':
    sys.exit(main())
