from hashtable.hashtable import *
from hashtable.linked_list import LinkedList
def test_hash_create():
    ht = Hashtable(10)
    assert ht.map == [None, None, None, None, None, None, None, None, None, None]

def test_hash_add():
    ht = Hashtable(1024)
    ht.add('name', 'Abdullah')
    assert ht.map[945].head.data == ('name', 'Abdullah')
    

def test_hash_get():
    ht = Hashtable(1024)
    ht.add('name', 'Abdullah')
    assert ht.get('name') == 'Abdullah'

def test_hash_get_not():
    ht = Hashtable(1024)
    assert ht.get('name') == None

def test_hash_add_collision():
    ht = Hashtable(1024)
    ht.add('name', 'Abdullah')
    ht.add('mane', 'not Abdullah')
    assert ht.get('name') == 'Abdullah'
    assert ht.get('mane') == 'not Abdullah'

def test_hash_hash():
    ht = Hashtable(1024)
    key = 'name'
    assert ht.hash(key) == 945

def test_hash_contains():
    ht = Hashtable(1024)
    ht.add('name', 'Abdullah')
    assert ht.contains('name') == True
    assert ht.contains('phone') == False