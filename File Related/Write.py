# Get input from user
user_input = input("Enter text to write to file: ")
f=input("Enter the file name (Ex: output.txt): ")

# Open a file in write mode
with open(f, "w") as file:
    # Write the user input to the file
    file.write(user_input)

print("Data written to file successfully.")
