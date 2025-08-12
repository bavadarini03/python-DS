class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
class queue:
    def __init__ (self):
        self.front=None
        self.rear=None
    def is_empty(self):
        return self.front is None
    def enqueue(self,data):
        newNode=Node(data)
        if self.rear is None:
            self.front=self.rear=newNode
            return
        self.rear.next=newNode
        self.rear=newNode
    def dequeue(self):
        if self.is_empty():
            return None
        data=self.front.data
        self.front=self.front.next
        if self.front is None:
            self.rear=None
        return data
    def peek(self):
        if self.is_empty():
            return None
        return self.front.data
    def sixe(self):
        count=0
        current=self.front
        while current:
            count+=1
            current=current.next
        return count
q=queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("queue elements:",end=" ")
while not q.is_empty():
    print(q.dequeue(),end=" ")
print("\n IS the queue empty?",q.is_empty())
