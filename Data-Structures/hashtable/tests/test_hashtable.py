from hashtable.hashtable import *
from hashtable.linked_list import LinkedList
from challenges.hashmap_repeated_word import *
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


def test_hashmap_repeated_word_test():
    input_string1 = 'Once upon a time, there was a brave princess who...'
    input_string2= 'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...'
    input_string3 = 'It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...'
    input_string4 = ''
    input_string5 = 'Hi I am Abdullah'
    assert hashmap_repeated_word(input_string1) == 'a'
    assert hashmap_repeated_word(input_string2) == 'it'
    assert hashmap_repeated_word(input_string3) == 'summer'
    assert hashmap_repeated_word(input_string4) == None
    assert hashmap_repeated_word(input_string5) == None
