from stacks_and_queues.stacks_and_queues import *
from challenges.PseudoQueue import *
from challenges.fifo_animal_shelter import *
from challenges.multi_bracket_validation import *
import pytest



def test_push_pop_to_stack():
    stack = Stack()
    assert stack.top == None
    stack.push(1)
    assert stack.top.value == 1
    stack.push(2)
    stack.push(3)
    assert stack.top.value == 3
    assert stack.top.next.value == 2
    assert stack.top.next.next.value == 1
    stack.pop()
    assert stack.top.value == 2
    stack.pop()
    stack.pop()
    assert stack.top == None
    stack.push(2)
    stack.push(3)

def test_peak_empty_stack():
    stack = Stack()
    assert stack.is_empty() == True
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.peek() == 3

def test_pop_empty_stack():
    with pytest.raises(ValueError):
        stack = Stack()
        assert stack.pop()




def test_enqueue_dequeue_peak_queue():
    queue = Queue()
    queue.enqueue(1)
    assert queue.rear.value == 1
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    assert queue.front.next.next.next.value == 4
    queue.dequeue()
    assert queue.front.next.next.value == 4
    assert queue.rear.value == 4
    assert queue.front.value == 2
    assert queue.peak() == 2
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    assert queue.front == None

def test_empty_stack():
    queue = Queue()
    assert queue.is_empty() == True

def test_dequeue_empty_stack():
    with pytest.raises(ValueError):
        queue = Queue()
        assert queue.dequeue()

def test_pseudoqueue():
    my_queue = PseudoQueue()
    my_queue.enqueue(20)
    my_queue.enqueue(15)
    my_queue.enqueue(10)
    my_queue.enqueue(5)

    assert my_queue.dequeue() == 20
    assert my_queue.dequeue() == 15
    assert my_queue.dequeue() == 10
    assert my_queue.dequeue() == 5

def test_pseudoqueue_empty():
    my_queue = PseudoQueue()
    my_queue.enqueue(5)
    assert my_queue.dequeue() == 5


def test_AnimalShelter_enqueue():
    animals = AnimalShelter()
    assert animals.enqueue(cat)
    assert animals.front.name == 'cat'
    assert animals.rear.name == 'cat'
    assert animals.enqueue(dog)
    assert animals.front.name == 'cat'
    assert animals.rear.name == 'dog'
    assert animals.Animal_enqueue('elephant') == 'Add dog or cat'
    assert animals.front.name == 'cat'
    assert animals.rear.name == 'dog'


def test_AnimalShelter_enqueue():
    animals = AnimalShelter()
    assert animals.dequeue('human') == 'Your input is not in the Animal shelter'
    assert animals.dequeue(cat) == 'Your input is not in the Animal shelter'
    animals.enqueue(cat)
    animals.enqueue(dog)
    animals.enqueue(cat)
    animals.enqueue(dog)
    assert animals.dequeue(cat) == 'cat'
    assert animals.dequeue(cat) == 'cat'
    assert animals.dequeue(cat) == 'Your input is not in the Animal shelter'
    assert animals.dequeue(dog) == 'dog'
    assert animals.dequeue(dog) == 'dog'
    assert animals.dequeue(dog) == 'Your input is not in the Animal shelter'


def test_multi_bracket():
    assert multi_bracket_validation('[]()[]') == True
    assert multi_bracket_validation('{}') == True
    assert multi_bracket_validation('{}(){}') == True
    assert multi_bracket_validation('()[[Extra Characters]]') == True
    assert multi_bracket_validation('(){}[[]]') == True
    assert multi_bracket_validation('{}{Code}[Fellows](())') == True
    assert multi_bracket_validation('[({}]') == False
    assert multi_bracket_validation('(](') == False
    assert multi_bracket_validation('{(})') == False
    




