import sys
print("Command line arguments")
print("No. of arguments: ",len(sys.argv),"arguments")
print("Argument list")
i=1
print(sys.argv)
for arg in sys.argv:
    print(i," ",arg)
    i=i+1
