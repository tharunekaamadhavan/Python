class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DLL:
    def __init__(self):
        self.head=None

    def insert_to_empty(self,data):
        if self.head is None:
            newnode=Node(data)
            self.head=newnode

    def insert(self,newnode):
        if self.head is None:
            self.head=newnode
        else:
            lastnode=self.head
            while lastnode.next:
                lastnode=lastnode.next
            lastnode.next=newnode
            newnode.prev=lastnode

    def insertafter(self,data,value):
        lastnode=self.head
        while lastnode:
            if lastnode.data==value:
                break
            lastnode=lastnode.next
        if lastnode is None:
            print("The LL is empty")
        else:
            newnode=Node(data)
            newnode.next=lastnode.next
            newnode.prev=lastnode
            newnode.prev.next=newnode
            lastnode.next=newnode

    def insertbefore(self,data,value):
        lastnode=self.head
        while lastnode:
            if lastnode.data==value:
                break
            lastnode=lastnode.next
        if lastnode is None:
            print("LL is empty")
        else:
            newnode=Node(data)
            newnode.prev=lastnode.prev
            newnode.next=lastnode
            newnode.prev.next=newnode
            lastnode.prev=newnode

    def deleteatstart(self):
        if self.head is None:
            print("LL has no element")
            return
        if self.head.next is None:
            self.head=None
            return
        self.head=self.head.next
        self.head.prev=None

    def deletespecific(self,value):
        lastnode=self.head
        while lastnode:
            if lastnode.data==value:
                break
            lastnode=lastnode.next
        if lastnode is None:
            print("element not in list")
        else:
            lastnode.prev.next=lastnode.next
            lastnode.next.prev=lastnode.prev

    def deleteatend(self):
        if self.head is None:
            print("ll is empty")
        n=self.head
        while n.next is not None:
            n=n.next
        n.prev.next=None


    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        else:
            currentnode=self.head
            while currentnode:
                print(currentnode.data)
                currentnode=currentnode.next

dll=DLL()
dll.insert_to_empty(0)
dll.insert(Node(10))
dll.insert(Node(20))
dll.insert(Node(30))
dll.insertafter(25,20)
dll.insertafter(27,25)
dll.insertbefore(26,27)
dll.deleteatstart()
dll.deletespecific(20)
dll.deleteatend()
dll.print()
