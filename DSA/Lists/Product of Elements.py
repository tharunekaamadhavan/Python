import sys

def product(a, n):
    x = 1.0
    for i in range(0, n):
        x = x * a[i]
    return x

a = [1, 2, 3, 4, 5]
n = len(a)
result = product(a, n)
print("Product of elements:", result)
print("Size of x:", sys.getsizeof(result))
