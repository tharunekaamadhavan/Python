dobo = input("Enter the file name: ")

vowels = 0
consonants = 0
digits = 0
words = 0

with open(dobo, 'r') as file:
    for line in file:
        for word in line.split():
            words += 1
            for char in word:
                if char.isdigit():
                    digits += 1
                elif char.isalpha():
                    if char.lower() in ['a', 'e', 'i', 'o', 'u']:
                        vowels += 1
                    else:
                        consonants += 1

print("No. of Vowels:", vowels)
print("No. of Consonants:", consonants)
print("No. of Digits:", digits)
print("No. of Words:", words)
