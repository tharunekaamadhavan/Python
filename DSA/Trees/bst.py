from binarytree import bst,Node
my_bst=bst(height=2,is_perfect=True)
print("Randomly generated tree")
print(my_bst)
print("Deletion")
del my_bst[1]
print(my_bst)
print("Insertion")
my_bst[2]=Node(6,left=Node(78),right=Node(3))
print(my_bst)
print("inorder")
print(my_bst.inorder)