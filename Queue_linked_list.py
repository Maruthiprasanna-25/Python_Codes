class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def enqueue(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
    def isEmpty(self):
        return self.head==None
    def dequeue(self):
        if self.isEmpty():
            print("No elements Exist for dequeue")
        else:
            self.head=self.head.next
    def peek(self):
        if self.isEmpty():
            print("No elements Exist")
        else:
            return self.head.data
q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.dequeue()

print(q.peek())