file=input("Enter the file name: ")
with open(file,"w") as f:
    f.write(input("Enter content: "))
filey=input("Enter the file name: ")
with open(filey,"w") as ff, open(file,"r") as f:
    ff.write(input("Enter content: "))
    while True:
        block=f.readlines()
        if not block:
            break
        ff.write(str(block))
    print("copy done")
    
