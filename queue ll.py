class Node():
    def __init__ (self,data):
        self.data=data
        self.next=None
class linkedlist():
    def __init__(self):
        self.head=None
    def empty(self):
        if self.head is None:
            return True
        else:
            return False
    def enqueue(self,data):
        newnode=Node(data)
        if self.empty():
            self.head=newnode
        else:
            n=self.head
            while n.next:
                n=n.next
            n.next=newnode
    def dequeue(self):
        if self.head is None:
            print("Queue is empty")
        n=self.head
        if n:
            ele=n.data
            self.head=n.next
            n=None
            return ele
    def tail(self):
        current=self.head
        while current.next:
            current=current.next
        
        
        print("Tail element:",current.data)
    def peek(self):
        print("First element of queue:",self.head.data)
    
    

    def print(self):
        n=self.head
        while n:



            print(n.data)
            n=n.next
ll=linkedlist()
ll.enqueue(3)
ll.enqueue(2)
ll.enqueue(6)
ll.enqueue(4)
print("Elements in queue:")
ll.print()
print("Element dequeued:",ll.dequeue())
print("Queue after elements dequeued:")
ll.print()
ll.tail()
ll.peek()


