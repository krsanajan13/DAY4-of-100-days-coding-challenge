class Mystack:
    def __init__(self,cap):
        self.cap=cap
        self.top=-1
        self.stack=[0]*cap

    def push(self,element):
        if self.isFull():
            print("stack Overflow")
            return
        self.top+=1
        self.stack[self.top]=element

    def isFull(self):
        return self.top==self.cap

    def pop(self):
        if self.isEmpty():
            print("stack Undeflow")
            return -1
        element=self.stack[self.top]
        self.top-=1
        return element
    def isEmpty(self):
        return self.top==-1

    def peek(self):
        if self.isEmpty():
            print("stack Undeflow")
            return -1
        element = self.stack[self.top]
        return element

    def display(self):
        for i in range(self.top,-1,-1):
            print(self.stack[i],end=' ')

s=Mystack(5)
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.display()
print()
s.pop()
s.display()




