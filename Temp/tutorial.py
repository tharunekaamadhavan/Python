'''a=input("Enter name: ")
b=input("What's your favourite color? ")
print(a,"likes",b)
a=eval(input("Enter weight in pounds: "))
b=a/2.205
print("Your weight in kg: ",b)
a="hellello"
a.find('o')
print(1435//4)
name=str(input("Enter name: "))
if len(name)<3:
    print("Name must be at least 3 characters long")
elif len(name)>50:
    print("Name can be maximum of 50 characters")
else:
    print("Name looks good!")
w=int(input("Weight: "))
c=str(input("(L)bs or (K)g: "))
if c=="K" or c=="k":
    g=w/0.45
    print(f"You are {g} pounds")
else:
    g=w*0.45
    print(f"You are {g} kg")
secret=5

i=1
while i<=3:
    guess=int(input("Guess: "))
    if guess==secret:
        print("You win!")
        break
    else:
        print("Try again")
        i+=1
else:
    print("You loose")
command=""
started=False
while True:
    command=input("> ").lower()
    if command=="start":
        if started:
            print("Car already started!")
        else:
            started= True
            print("Car started")
    elif command=="stop":
        if not started:
            
            print("Car already stopped")
        else:
            started= False 
            print("Car stopped!")
    elif command=="help":
        print("""start- to start the car
stop- to stop the car
quit- to end""")
    elif command=="quit":
        print("Ended")
        break
    else:
        print("Sorry I don't understand")
num=[2,2,2,2,5]
for i in num:
    for j in range(i):
        print("x",end="")
    print()
num=[5,4,7,8,3,7,8,4]
maxi=num[0]
for i in num:
    if i>maxi:
        maxi=i
print("Max number: ",maxi)
num=[5,4,7,8,3,7,8,4]
num.sort(reverse=True)
print(num)
a=num.copy()
num.sort()
print(a)
print(num)
num=[5,4,7,8,3,7,8,4]
d=[]
for i in num:
    if i not in d:
        d.append(i)
print(d)'''
number=str(input("Phone: "))
d={'1':'one','2':'two','3':'three','4':'four'}
o=""
for i in number:
    o+=d.get()

