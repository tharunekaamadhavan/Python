a=[57,-57,57,57]
def absvalue(dig):
    return abs(dig)
b=
a.sort(key = absvalue)
print(a)
a.sort(key = lambda dig: abs(dig))
print(a)
