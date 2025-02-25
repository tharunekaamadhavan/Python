class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LL:
    def __init__(self):
        self.head=None

    def insert(self,newnode):
        if self.head is None:
            self.head=newnode
        else:
            lastnode=self.head
            while lastnode.next:
                lastnode=lastnode.next
            lastnode.next=newnode

    def add_beginning(self,newnode):
        newnode.next=self.head
        self.head=newnode

    def add_after(self,data,x):
        lastnode=self.head
        while lastnode:
            if x==lastnode.data:
                break
            lastnode=lastnode.next
        if lastnode is None:
            print(x," is not in list")
        else:
            newnode=Node(data)
            newnode.next=lastnode.next
            lastnode.next=newnode

    def add_before(self,data,x):
        if self.head is None:
            print("LL is empty")
            return
        if self.head.data==x:
            newnode=Node(data)
            newnode.next=self.head
            self.head=newnode
            return
        lastnode=self.head
        while lastnode.next:
            if lastnode.next.data==x:
                newnode=Node(data)
                newnode.next=lastnode.next
                lastnode.next=newnode
                return
            lastnode=lastnode.next
        print(x,"is not in LL")

    def print(self):
        currentnode=self.head
        while currentnode:
            print(currentnode.data)
            currentnode=currentnode.next

l=LL()
l.insert(Node("A"))
l.insert(Node("B"))
l.add_beginning(Node("C"))
l.add_after("D","A")
l.add_before("B","E")
l.add_before("C","F")
l.print()
