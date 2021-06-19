from challenges.ll_zip.ll_zip import zipLists
from linked_list import __version__
from linked_list.linked_list import LinkedList , Node
import pytest


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

######################################## insert before ##########################################
def test_insert_Before_1(linked_list_1):
    linked_list_1.insertBefore(3, 5)
    assert linked_list_1.head.next.value is 5
def test_insert_Before_2(linked_list_1):
    linked_list_1.insertBefore(1, 5)
    assert linked_list_1.head.value is 5
def test_insert_Before_3(linked_list_1):
    linked_list_1.insertBefore(2, 5)
    assert linked_list_1.head.next.next.value is 5
def test_insert_Before_4(linked_list_1):
    with pytest.raises(ValueError):
        linked_list_1.insertBefore(4, 5)

######################################## insert after ##########################################
def test_insert_After_1(linked_list_1):
    linked_list_1.insertAfter(3, 5)
    assert linked_list_1.head.next.next.value is 5
def test_insert_After_2(linked_list_1):
    linked_list_1.insertAfter(2, 5)
    assert linked_list_1.head.next.next.next.value is 5
def test_insert_After_3():
    LL = LinkedList()
    LL.append(1)
    LL.append(2)
    LL.append(2)
    LL.insertAfter(2, 5)
    assert LL.head.next.next.value is 5
def test_insert_After_4(linked_list_1):
    with pytest.raises(ValueError):
        linked_list_1.insertAfter(4, 5)

######################################## kth_from_end ##########################################
def test_kth_from_end_1(linked_list_2):
    actual = linked_list_2.kth_from_end(0)
    expected = 2
    assert actual == expected
    assert linked_list_2.kth_from_end(2) == 3
def test_kth_from_end_2(linked_list_2):
    with pytest.raises(ValueError):
        linked_list_2.kth_from_end(6)
        linked_list_2.kth_from_end(-1)
        linked_list_2.kth_from_end(4)

############################################# ll_zip ##########################################
def test_ll_zip_1(linked_list_3,linked_list_4):
    linked_list_3.append(2)
    linked_list_4.append(4)
    assert str(zipLists(linked_list_3,linked_list_4)) == '{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> { 4 } -> Null'
def test_ll_zip_2(linked_list_3,linked_list_4):
    linked_list_4.append(4)
    assert str(zipLists(linked_list_3,linked_list_4)) == '{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 4 } -> Null'
def test_ll_zip_3(linked_list_3,linked_list_4):
    linked_list_3.append(2)
    assert str(zipLists(linked_list_3,linked_list_4)) == '{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> Null'
def test_ll_zip_4():
    LL1 = LinkedList()
    LL2 = LinkedList()
    assert str(zipLists(LL1,LL2)) == 'None'
def test_ll_zip_5():
    LL1 = LinkedList()
    LL1.append(1)
    LL2 = LinkedList()
    assert str(zipLists(LL1,LL2)) == '{ 1 } -> Null'
def test_ll_zip_6():
    LL1 = LinkedList()
    LL2 = LinkedList()
    LL2.append(1)
    assert str(zipLists(LL1,LL2)) == '{ 1 } -> Null'


    

######################################## fixtures ##########################################
@pytest.fixture
def linked_list_1():
    LL = LinkedList()
    LL.append(1)
    LL.append(3)
    LL.append(2)
    return LL

@pytest.fixture
def linked_list_2():
    LL = LinkedList()
    LL.append(1)
    LL.append(3)
    LL.append(8)
    LL.append(2)
    return LL


@pytest.fixture
def linked_list_3():
    LL = LinkedList()
    LL.append(1)
    LL.append(3)
    return LL

@pytest.fixture
def linked_list_4():
    LL = LinkedList()
    LL.append(5)
    LL.append(9)
    return LL
