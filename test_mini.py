
import sys
import ast
import meta
steps = []
var = [1, 2]
def append_me(x):
    var = [3, 4]
    var.append(x)
    return var
def append_to_me(x):
    var = [3, 4]
    x.extend(var)
    return var
print var
print append_me(var)
print var
print append_to_me(var)
print var
