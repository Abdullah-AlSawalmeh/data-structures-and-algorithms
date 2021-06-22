from stacks_and_queues.stacks_and_queues import Stack,Node


class PseudoQueue:
    def __init__(self):

        # Two Stacks
        self.push_stack = Stack()
        self.pop_stack = Stack()

    def enqueue(self, item):
        self.push_stack.push(item)

    def dequeue(self):

        if self.pop_stack.is_empty():
            while self.push_stack.top != None:
                self.pop_stack.push(self.push_stack.pop())
        return self.pop_stack.pop()
        

my_queue = PseudoQueue()
my_queue.enqueue(10)
print(my_queue.dequeue())
my_queue.enqueue(15)
print(my_queue.dequeue())


# my_queue.enqueue(20)
# my_queue.enqueue(5)

# print(my_queue.dequeue())
# print(my_queue.dequeue())
# print(my_queue.dequeue())
# print(my_queue.dequeue())



