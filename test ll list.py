class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class list():
    def __init__(self):
        self.head=None
    def insert(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            n=self.head
            while n.next:
                n=n.next
            n.next=newnode
    def print(self):
        n=self.head
        while n:
            print(n.data)
            n=n.next
l=list()
l.insert(4)
l.insert(5)
l.insert(6)
l.insert(2)
l.insert(8)
l.print()