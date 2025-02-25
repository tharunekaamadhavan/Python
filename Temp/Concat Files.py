# Get input for two file names from the user
file1 = input("Enter the name of the first file: ")
file2 = input("Enter the name of the second file: ")
with open(file1, "w") as f1,open(file2, "w") as f2:
    f1.write(input("Enter content: "))
    f2.write(input("Enter content: "))
with open(file1, "r") as f1,open(file2, "r") as f2:
    
    file1_contents = f1.read()
    file2_contents = f2.read()


# Concatenate the contents of the two files
concatenation = file1_contents + file2_contents

# Get input for the output file name from the user
output_file = input("Enter the name of the output file: ")

# Open the output file in write mode
with open(output_file, "w") as op:
    # Write the concatenated contents to the output file
    op.write(concatenation)

print("Files concatenated successfully!")
