def gcd(a, b):
    """
    Recursive function to compute the greatest common divisor (GCD) of two numbers.

    Args:
    a (int): First number
    b (int): Second number

    Returns:
    int: GCD of a and b.
    """

    if b == 0:  # Base case: b is 0
        return a
    else:
        return gcd(b, a % b)  # Recursive call to gcd with b and the remainder of a divided by b


# Input numbers
a = 122
b = 96

# Calculate GCD
result = gcd(a, b)

# Output the result
print(f"The GCD of {a} and {b} is {result}")
