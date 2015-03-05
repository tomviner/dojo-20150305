import sys
import ast
import meta


def replace_variables(code):
    for node in ast.walk(code):
        if hasattr(node, 'id'):
            node.id = node.id[0]
        elif hasattr(node, 'name'):
            node.name = node.name[0]
    return code


steps = [replace_variables]


def minify(filename):
    with open(filename) as f:
        code = f.read()
    result = ast.parse(code)
    for step in steps:
        result = step(result)
    return meta.dump_python_source(result)

if __name__ == '__main__':
    filename = sys.argv[-1]
    if sys.argv[1] == '-t':
        exec(minify(filename))
    else:
        print minify(filename)
