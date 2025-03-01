try:
    n=int(input("Enter numerator: "))
    d=int(input("Enter denominator: "))
    q=n/d
    print("Quotient: ",q)
except ZeroDivisionError:
    print("Zero can't be a denominator")
except ValueError:
    print("That was not  a number")
finally:
    print("Thank you")
