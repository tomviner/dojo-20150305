import re
import __builtin__
import sys
import ast
import meta
import string


RESERVED_VARS = dir(__builtin__)


def _varname_iterator():
    var_incr = 0
    while True:
        for letter in string.ascii_letters:
            yield letter + str(var_incr if var_incr > 0 else '')
        var_incr += 1
varname_iterator = _varname_iterator()


vars = {}


def map_var(name):
    if name in RESERVED_VARS:
        return name
    elif name in vars:
        return vars[name]
    else:
        vars[name] = varname_iterator.next()
        return vars[name]


def replace_variables(code):
    for node in ast.walk(code):
        if hasattr(node, 'asname'):
            node.asname = map_var(node.name)
        elif hasattr(node, 'id'):
            node.id = map_var(node.id)
        elif hasattr(node, 'name'):
            node.name = map_var(node.name)
    return code


steps = [replace_variables]


def minify(filename):
    with open(filename) as f:
        code = f.read()

    result = ast.parse(code)
    for step in steps:
        result = step(result)
    codestr = meta.dump_python_source(result)
    codestr = re.sub('el\s+if ', 'elif ', codestr)
    return codestr


if __name__ == '__main__':
    filename = sys.argv[-1]
    if sys.argv[1] == '-t':
        exec(minify(filename))
    else:
        print minify(filename)
