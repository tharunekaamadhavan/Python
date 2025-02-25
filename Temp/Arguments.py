import sys

# Check if the number of arguments is correct
if len(sys.argv) != 3:
    print("Usage: python script.py <arg1> <arg2>")
    sys.exit(1)

# Extract command-line arguments
arg1 = sys.argv[1]
arg2 = sys.argv[2]

# Perform operation using command-line arguments
result = int(arg1) + int(arg2)

# Display result
print("Result:", result)

