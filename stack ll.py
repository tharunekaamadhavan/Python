class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class stack():
    def __init__(self):
        self.head=None
    def push(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
    def pop(self):
        if self.head is None:
            return None
        else:
            n=self.head
            ele=n.data
            self.head=n.next
            n=None
            return ele
    def peek(self):
        if self.head is None:
            return None
        else:
            print("First element:",self.head.data)
    def disp(self):
        if self.head is None:
            print("empty")
        else:
            n=self.head
            while n:
                print(n.data)
                n=n.next
s=stack()
s.push(5)
s.push(2)
s.push(7)
s.push(3)
s.push(8)
r=s.pop()
print("Element removed:",r)
s.peek()
s.disp()