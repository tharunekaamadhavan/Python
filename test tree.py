from binarytree import *
nodes=int(input("Enter the number of nodes:"))
values=[]
for i in range(nodes):
    a=int(input("Enter value:"))

    values.append(a)
my_bst=bst(height=2,is_perfect=True)
print(my_bst)