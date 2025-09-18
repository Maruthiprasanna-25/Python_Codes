class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def addLast(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
    def addFirst(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head = newnode
    def findIndex(self, idx):
        i=0
        temp=self.head
        while i<idx:
            i+=1
            temp=temp.next
        return temp
    def addIndex(self, idx,data):
        if idx==0:
            self.addFirst(data)
        else:
            newnode=Node(data)
            temp=self.findIndex(idx-1)
            temp2=temp.next
            temp.next=newnode
            newnode.next=temp2
    def searchNode(self, key):
        temp=self.head
        while temp!=None:
            if temp.data==key:
                return True
            temp=temp.next
        return False
    def delFirst(self):
        self.head = self.head.next
    def delLast(self):
        if self.head == self.tail:
            self.head,self.tail=None,None
            return
        temp = self.head
        prev=None
        while temp != self.tail:
            prev=temp
            temp = temp.next
        prev.next = None
        self.tail = prev
    def findIndex(self, idx):
        i=0
        temp=self.head
        while i<idx:
            i+=1
            temp=temp.next
        return temp

    def deleteValue(self,val):
        if self.head.data == val:
            self.head = self.head.next
            return
        temp = self.head
        prev=None
        while temp != None:
            if temp.data == val:
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next
    def display(self):
        temp = self.head
        while temp!=None:
            print(temp.data,end=" ")
            temp = temp.next
        print()
    def findsize(self):
        temp=self.head
        count=0
        while temp!=None:
            count+=1
            temp=temp.next
        return count
if __name__ == "__main__":
    ll = LinkedList()
    ll.addLast(9)
    ll.addLast(10)
    ll.addFirst(5)
    ll.addFirst(3)
    ll.addIndex(1, 7)
    ll.addIndex(0, 1)
    ll.display()
    ll.delFirst()
    ll.delLast()
    ll.deleteValue(7)
    ll.display()
    res=ll.findsize()
    print(res)