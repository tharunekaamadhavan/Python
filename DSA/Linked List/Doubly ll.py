class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class Doublyll:
    def __init__(self):
        self.head=None

    def insert(self,newnode):
        if self.head is None:
            self.head=newnode
        else:
            lastnode=self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode=lastnode.next
            lastnode.next=newnode
            newnode.prev=lastnode
            #print("newnode previous",newnode.prev.data)
            #print("Newnode Next",newnode.next)
             
    def delatspecific(self,value):
        lastnode=self.head
        while lastnode is not None:
            if lastnode.data==value:
                break
            lastnode=lastnode.next
        if lastnode is None:
            print("Value is not present in the list")
        else:
            lastnode.previ.next=lastnode.next
            lastnode.next.prev=lastnode.prev
            
    def Display(self):
        if self.head is None:
            print("The list is empty")
            return
        else:
            currentnode = self.head
            while currentnode is not None:
                print(currentnode.data)
                currentnode = currentnode.next
        print("\n")

firstnode=Node(10)
doublyll=Doublyll()
doublyll.insert(firstnode)
secondnode=Node(20)
doublyll.insert(secondnode)
thirdnode=Node(30)
doublyll.insert(thirdnode)
doublyll.delatspecific(20)
doublyll.Display()
