
try:
    age=int(input("Enter age: "))
    if age<18:
        raise ValueError("Sorry u r not eligible to vote")
    print("U r eligible to vote")
except:
    print("That was not a number")
finally:
    print("Thank u")
