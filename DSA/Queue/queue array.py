class queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,data):
        self.queue.append(data)
    def dequeue(self):
        self.queue.pop(0)
    
    def peek(self):
        print(self.queue[0])
    def size(self):
        if self.check():
            print("empty")
        else:
            print(len(self.queue))
    def disp(self):
        print(self.queue)
    def check(self):
        return len(self.queue)==0
a=queue()
a.enqueue(4)
a.enqueue(6)
a.enqueue(3)
a.enqueue(7)
a.enqueue(2)
a.dequeue()
a.dequeue()
a.peek()
a.size()
a.disp()

