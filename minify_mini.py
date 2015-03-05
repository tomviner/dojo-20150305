
import sys
import ast
import meta
steps = []
def minify(filename):
    with open(filename)     as f    :    
        code = f.read()
    result = ast.parse(code)
    return meta.dump_python_source(result)
if (__name__ == '__main__'):
    minify(sys.argv[1])

