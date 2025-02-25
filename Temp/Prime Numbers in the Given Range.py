def isPrime(n):
    # Corner case
    if n <= 1:
        return False

    # Check from 2 to sqrt(n) for efficiency
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  # Return False if divisible

    return True  # Return True if no divisors found

# Function to print primes
def printPrime(n):
    for i in range(2, n + 1):
        if isPrime(i):
            print(i, end=" ")

# Driver code
if __name__ == "__main__":
    n = 50
    # Function calling
    printPrime(n)
