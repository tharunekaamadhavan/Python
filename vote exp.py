try:
    a=int(input("Enter age: "))
    if a<18:
        raise Exception("You are not eligible to vote")
    print("You are eligible to vote")
except ValueError:
    print("That was not a number")
finally:
    print("Thank you")
