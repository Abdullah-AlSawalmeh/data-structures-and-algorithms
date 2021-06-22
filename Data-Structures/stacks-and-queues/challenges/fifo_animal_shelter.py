class cat:
    name="cat"
    def __init__(self):
        self.name = "cat"
        self.next = None
        

class dog:
    name="dog"
    def __init__(self):
        self.name = "dog"
        self.next = None


class AnimalShelter:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        if value.name == 'dog' or value.name == 'cat':
            node = value()
            if not self.rear:
                self.front = node
                self.rear = node
            else:
                self.rear.next = node
                self.rear = node
        return "Add dog or cat"

    def dequeue(self,value):
        if  self.is_empty():
            return 'Your input is not in the Animal shelter'
        else:
            if self.front.name == value.name:
                temp = self.front
                self.front = self.front.next
                temp.next = None
                return temp.name
            else:
                temp = self.front
                while self.front.next:
                    if self.front.next.name == value.name:
                        temp2 = self.front.next
                        self.front.next = self.front.next.next
                        self.front = temp
                        temp2.next = None
                        return temp2.name
                    else:
                        self.front = self.front.next
                else:
                    self.front = temp
                    return "Your input is not in the Animal shelter"


    def peak(self):
        if  self.is_empty():
            raise ValueError("Enqueue elements to the queque")
        else:
            return self.front.name


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

    queue = AnimalShelter()
    queue.enqueue(cat)
    queue.enqueue(dog)
    queue.enqueue(cat)
    queue.enqueue(dog)
    # queue.enqueue(cat)
    # queue.enqueue(cat)
    # queue.enqueue(dog)
    print(queue.dequeue(cat))
    print(queue.dequeue(cat))
    print(queue.dequeue(cat))
    print(queue.dequeue(dog))
    print(queue.dequeue(dog))

    # print(queue.front.name)
    # print(queue.front.next.name)
    # print(queue.front.next.next.name)
    # print(queue.front.next.next.next.name)
    # print(queue.front.next.next.next.next.name)