# Stacks and Queues

<!-- Short summary or background information -->

### About Stacks

- A stack is a data structure that consists of Nodes. Each Node references the next Node in the stack, but does not reference its previous.

### About Queues

- Queue is a linear data structure that stores items in First In First Out (FIFO) manner. With a queue the least recently added item is removed first. A good example of queue is any queue of consumers for a resource where the consumer that came first is served first.

## Challenge

Define pop, push, peak and isempty for stack and enqueue, dequeue, peak and isempty for queue.

## Approach & Efficiency

- Pop O(1)
- Push O(1)
- Dequeue O(1)
  When you remove an item from a queue, you use the dequeue action. This is done with an O(1) operation in time because it doesn’t matter how many other items are in the queue, you are always just removing the front Node of the queue.

- Peek O(1) : When conducting a peek, you will only be inspecting the front Node of the queue.

- Typically, you want to check isEmpty before conducting a peek. This will ensure that an exception is not raised. Alternately, you can wrap the call in a try/catch block.

- IsEmpty O(1)
  Here is the pseudocode for isEmpty

## API

### Common terminology for a stack is

- Push - Nodes or items that are put into the stack are pushed
- Pop - Nodes or items that are removed from the stack are popped. When you attempt to pop an empty stack an exception will be raised.
- Top - This is the top of the stack.
- Peek - When you peek you will view the value of the top Node in the stack. When you attempt to peek an empty stack an exception will be raised.
- IsEmpty - returns true when stack is empty otherwise returns false.

- Stacks follow these concepts:

1. FILO: First In Last Out
2. Lifo: This means that the first item added in the stack will be the last item popped out of the stack.

![](https://learn1.open.ac.uk/mod/oublog/pluginfile.php/15/mod_oublog/message/162582/stack.png)

## Note:

- the topmost item is denoted as the top. When you push something to the stack, it becomes the new top. When you pop something from the stack, you pop the current top and set the next top as top.next.

- Common terminology for a queue is

- Enqueue - Nodes or items that are added to the queue.
- Dequeue - Nodes or items that are removed from the queue. If called when the queue is empty an exception will be raised.
- Front - This is the front/first Node of the queue.
- Rear - This is the rear/last Node of the queue.
- Peek - When you peek you will view the value of the front Node in the queue. If called when the queue is empty an exception will be raised.
- IsEmpty - returns true when queue is empty otherwise returns false.
- Queues follow these concepts:

- FIFO: First In First Out: This means that the first item in the queue will be the first item out of the queue.

- LILO: Last In Last Out: This means that the last item in the queue will be the last item out of the queue.

![](https://image.slidesharecdn.com/20140710stackqueue-150112072633-conversion-gate01/95/basic-data-structure-stackqueue-40-638.jpg?cb=1421047682)

```

```
