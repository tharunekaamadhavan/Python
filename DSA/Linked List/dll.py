class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class doubly():
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
            newnode.prev=n
    def insertatbeg(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
    def insertafter(self,data,value):
        n=self.head
        while n:
            if n.data==value:
                break
            n=n.next
        if n is None:
            print("not present")
        else:
            newnode=Node(data)
            newnode.next=n.next
            newnode.prev=n
            n.next.prev=newnode
            n.next=newnode
        
    def print(self):
        if self.head is None:
            print("Empty")
        else:
            n=self.head
            while n:
                print(n.data)
                n=n.next
                print("\n")
dl=doubly()
dl.insert(53)
dl.insert(52)
dl.insertatbeg(42)
dl.insertafter(6,53)
dl.print()
            