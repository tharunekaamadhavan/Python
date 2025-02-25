class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class ll():
    def __init__(self):
        self.head=None
    def insert(self,newnode):
        if self.head is None:
            self.head=newnode
        else:
            n=self.head
            while True:
                if n.next is None:
                    break
                n=n.next
            n.next=newnode
    def disp(self):
        n=self.head
        while True:
            if n is None:
                break
            print(n.data)
            n=n.next
firstnode=Node(32)
l=ll()
l.insert(firstnode)
secondnode=Node(43)
l.insert(secondnode)
thirdnode=Node(54)
l.insert(thirdnode)
l.disp()
        