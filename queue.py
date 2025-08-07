class MyQueue:
    def __init__(self,capacity):
        self.capacity=capacity
        self.queue=[0]*capacity
        self.front=0
        self.rear=0

    def enQueue(self,element):
        if self.isFull()==True:
            print("Queue is already full")
            return
        self.queue[self.rear]=element
        self.rear=self.rear+1

    def deQueue(self):
        if self.isEmpty()==True:
            print("Queue is empty")
            return -1
        self.element=self.queue[self.front]
        self.front=self.front+1
        return self.element

    def isFull(self):
        return self.rear==self.capacity

    def isEmpty(self):
        return self.rear==self.front

    def display(self):
        if self.isEmpty()==True:
            print("Queue is Empty")
            return
        for i in range(self.front,self.rear):
            print(self.queue[i],end=' ')




q=MyQueue(5)
q.enQueue(10)
q.enQueue(20)
q.enQueue(30)
q.enQueue(40)
q.enQueue(50)
q.display()
print()
q.deQueue()
q.deQueue()
q.display()
