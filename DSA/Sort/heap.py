from binarytree import *
class BinaryHeap:
    def heapify(self):
        self.tree=heap(height=2,is_max=True,is_perfect=True)
        print(self.tree)
    def parent(self):
        print("parent node")
        print(self.tree.val,self.tree.left.val,self.tree.right.val)
    def left(self):
        print("left sub tree")
        
        print(self.tree.left)
        print("Nodes=",self.tree.left.values)
    def right(self):
        print(self.tree.right)
        print(self.tree.right.values)
    def size(self):
        print(self.tree.size)
    def get(self):
        print("max:",self.tree.max_node_value)
        print("min:",self.tree.min_node_value)
b=BinaryHeap()
print("1.parent nodes\n2.left subtrees\n3.right\n4.size\n5.max and min")
ch=int(input("Enter choice"))
b.heapify()
if ch==1:
    b.parent()
elif ch==2:
    b.left()
elif ch==3:
    b.right()
elif ch==4:
    b.size()
elif ch==5:
    b.get()
else:
    print("Invalid")
