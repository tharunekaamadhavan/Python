def check_voting_eligibility(age):
    if age < 18:
        raise ValueError("Sorry, you are not eligible to vote!")
    else:
        print("You are eligible to vote. Please cast your vote!")

# Example usage
try:
    age = int(input("Enter your age: "))
    check_voting_eligibility(age)
except ValueError as e:
    print(e)
