class Node: 
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        # self.top_temp = None
        self.top = None
    def push(self, value):
        node = Node(value)
        node.next = self.top
        # self.top_temp = self.top
        self.top = node
    def pop(self):
        if not self.is_empty():
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value
        else:
            self.top = None
            raise ValueError("Nothing to pop") 
    def peek(self):
        if not self.is_empty():
            return self.top.value
        else:
            raise ValueError("Nothing to show") 

    def is_empty(self): 
        return self.top == None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, value):
        node = Node(value)
        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if  self.is_empty():
            raise ValueError("Enqueue elements to the queque")
        else:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value
    def peak(self):
        if  self.is_empty():
            raise ValueError("Enqueue elements to the queque")
        else:
            return self.front.value
    def is_empty(self):
        return self.front == None
 


if __name__ == "__main__":
    # stack = Stack()
    # stack.push(1)
    # stack.push(2)
    # stack.push(3)
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    # print(queue.dequeue())