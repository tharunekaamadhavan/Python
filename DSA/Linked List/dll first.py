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
                
   
    #Delete element from the end
    def deleteatend(self):
        if self.head is None:
            print("Linked list is empty, No element to delete")
            return
        #checks whether the linked list contain only one node
        if self.head.next is None:
            self.head=None
            return
        lastnode=self.head
        while lastnode.next is not None:
            lastnode=lastnode.next
        lastnode.prev.next=None
            

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
doublyll.deleteatend()
doublyll.Display()
