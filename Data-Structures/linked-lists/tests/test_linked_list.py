from linked_list import __version__
from linked_list.linked_list import LinkedList , Node


def test_version():
    assert __version__ == '0.1.0'

def test_node():
    node = Node(1)
    assert node.value == 1
    assert node.next == None

def test_empty_LL():
    LL = LinkedList()
    assert LL.head is None

def test_insert():
    LL = LinkedList()
    LL.insert(1)
    LL.insert(2)
    LL.insert(3)
    assert LL.head.value is 3
    assert LL.head.next.value is 2
    assert LL.head.next.next.value is 1

def test_append():
    LL = LinkedList()
    LL.append(1)
    LL.append(2)
    LL.append(3)
    assert LL.head.value is 1
    assert LL.head.next.value is 2
    assert LL.head.next.next.value is 3

def test_append_insert():
    LL = LinkedList()
    LL.append(4)
    LL.append(5)
    LL.append(6)
    LL.insert(3)
    LL.insert(2)
    LL.insert(1)
    assert LL.head.value is 1
    assert LL.head.next.value is 2
    assert LL.head.next.next.value is 3
    assert LL.head.next.next.next.value is 4
    assert LL.head.next.next.next.next.value is 5
    assert LL.head.next.next.next.next.next.value is 6

def test_includes():
    LL = LinkedList()
    LL.append(4)
    LL.append(5)
    LL.append(6)
    LL.insert(3)
    LL.insert(2)
    LL.insert(1)
    assert LL.includes(2) is True
    assert LL.includes(7) is False

def test_print():
    LL = LinkedList()
    assert str(LL) == 'Linked list is empty!'
    LL.append(4)
    LL.append(5)
    LL.append(6)
    LL.insert(3)
    LL.insert(2)
    LL.insert(1)
    assert str(LL) == '{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> { 6 } -> Null'
