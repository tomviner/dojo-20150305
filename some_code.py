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
    return var

def star(*args):
    print args

print var
print append_me(var)
print var
print append_to_me(var)
print var
