import sys
import ast
import meta


steps = [lambda x: x]


def minify(filename):
    with open(filename) as f:
        code = f.read()
    result = ast.parse(code)
    for step in steps:
        result = step(result)
    return meta.dump_python_source(result)

if __name__ == '__main__':
    print minify(sys.argv[1])
