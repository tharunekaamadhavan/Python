first=input("Enter first file name: ")
second=input("Enter second file name: ")
with open(first,"r")as f, open(second,"w") as g:
    while True:
        block=f.readlines()
        if not block:
            break
        g.write(block)
    print("copied")
