from binarytree import *
nodes=int(input("Enter the number of nodes:"))
values=[]
for i in range(nodes):
    a=int(input("Enter value:"))

    values.append(a)
my_tree=build(values)
print(my_tree)
print("Preorder:",my_tree.preorder)
print("Postorder:",my_tree.postorder)
print("ineorder:",my_tree.inorder)