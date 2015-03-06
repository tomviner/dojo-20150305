import sys
import ast
import meta


steps = []  # [replace_variables, remove_whitespace]

var = [1, 1 + 2]

def append_me(args):
    var = [3, 4]
    var.append(args)
    return var

def append_to_me(x):
    var = [3, 4]
    x.extend(var)
    pass
    return var

def star(*args):
    print args

def do_nothing():
    pass

def upper(upper=upper):
    print upper.upper()

print var
print append_me(var)
print var
print append_to_me(var)
print var
print do_nothing()
print upper('upper')
