#Create Node
#Create Linked List
#Add nodes to linked list
#Print Linked List
class Node:
        def __init__(self,data):
                self.data=data
                self.next=None

# A Linked List class with a single head node:
class LinkedList:
        def __init__(self):
                self.head=None

        #Insert method for the linked list
        def insert(self,newnode):
                #head->John->None
                if self.head is None:
                        self.head=newnode
                else:
                        #head->John->Ben->None
                        lastnode=self.head
                        while True:
                                if lastnode.next is None:
                                        break
                                lastnode=lastnode.next
                        lastnode.next=newnode

         #data is the data we want to add after existing data x
        def add_before(self,data,x):
                #Find where x is present 
                if self.head is None:
                        print("Linked list is empty")
                        return
                if self.head.data==x:
                        newnode=Node(data)
                        newnode.next=self.head
                        self.head=newnode
                        return
                lastnode=self.head
                while lastnode.next is not None:
                        if lastnode.next.data==x:
                                newnode=Node(data)
                                newnode.next=lastnode.next
                                lastnode.next=newnode
                                return
                        lastnode=lastnode.next
                print("The data "+str(x)+" is not present in the list")
                        

        def printlist(self):
                #head->John->Ben->Mathew->None
                currentnode=self.head
                while True:
                        if currentnode is None:
                                break
                        print(currentnode.data)
                        currentnode=currentnode.next
firstnode=Node("John")
linkedlist=LinkedList()
linkedlist.insert(firstnode)
secondnode=Node("Ben")
linkedlist.insert(secondnode)
thirdnode=Node("Mathew")
linkedlist.insert(thirdnode)
fourthnode=Node("Peter")
linkedlist.add_before("Peter","Ben")
linkedlist.printlist()
