from hashtable.hashtable import *
from hashtable.linked_list import LinkedList
from challenges.hashmap_repeated_word import *
def test_hash_create():
    ht = Hashtable(10)
    assert ht.map == [None, None, None, None, None, None, None, None, None, None]

# def test_hash_add():
#     ht = Hashtable(1024)
#     ht.add('name', 'Abdullah')
#     assert ht.map[945].head.data == ('name', 'Abdullah')
#     

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


from challenges.tree_intersection import *


"""
Test Cases:
1. Verify that the function will return the intersected elements between two lists.
2. Verify that the function will return an empty set if the two lists have no interstion.
3. Verify that the function will return an empty set if one of the trees is empty.
4. Verify that the function will return the same tree if we compared the tree with itself.
"""

def test_tree_inter_yes():
    bt = BinaryTree()
    bt2 = BinaryTree()
    bt.root = Node(6)
    bt.root.right = Node(5)
    bt.root.left = Node(-1)
    bt.root.right.left = Node(7)
    bt.root.left.left = Node(10)
    bt.root.right.right = Node(3)
    
    bt2.root = Node(6)
    bt2.root.right = Node(5)
    bt2.root.left = Node(1)
    bt2.root.right.left = Node(6)
    bt2.root.left.left = Node(10)
    bt2.root.right.right = Node(2)

    assert tree_intersection(bt, bt2) == {10, 5, 6}

def test_tree_inter_no():
    bt = BinaryTree()
    bt2 = BinaryTree()
    bt.root = Node(6)
    bt.root.right = Node(5)
    bt.root.left = Node(-1)
    bt.root.right.left = Node(7)
    bt.root.left.left = Node(10)
    bt.root.right.right = Node(3)
    
    bt2.root = Node(20)
    bt2.root.right = Node(30)
    bt2.root.left = Node(40)
    bt2.root.right.left = Node(50)
    bt2.root.left.left = Node(60)
    bt2.root.right.right = Node(70)

    assert tree_intersection(bt, bt2) == set()

def test_tree_inter_empty1():
    bt = BinaryTree()
    bt2 = BinaryTree()
   
    
    bt2.root = Node(20)
    bt2.root.right = Node(30)
    bt2.root.left = Node(40)
    bt2.root.right.left = Node(50)
    bt2.root.left.left = Node(60)
    bt2.root.right.right = Node(70)

    assert tree_intersection(bt, bt2) == set()

def test_tree_inter_empty_both():
    bt = BinaryTree()
    bt2 = BinaryTree()

    assert tree_intersection(bt, bt2) == set()


def test_tree_inter_same():
    bt = BinaryTree()   
    
    bt.root = Node(20)
    bt.root.right = Node(30)
    bt.root.left = Node(40)
    bt.root.right.left = Node(50)
    bt.root.left.left = Node(60)
    bt.root.right.right = Node(70)

    assert tree_intersection(bt, bt) == {20, 30, 40, 50, 60, 70}




from challenges.left_join import *

"""
Test Cases:
1. Verify that the function will return the left join of 2 hashmaps.
2. Verify that the function will return None if the 2 hashmaps do not have left join.
3. Verify that the function will return None if the one of the hashmaps is empty.
"""

def test_left_join_normal():
    h1 = Hashtable(1024)
    h1.add('fond','enamored')        
    h1.add('wrath', 'anger')          
    h1.add('diligent', 'employed')    
    h1.add('outfit', 'garb')           
    h1.add('guide', 'usher')

    h2 = Hashtable(1024)
    h2.add('fond', 'averse')
    h2.add('wrath', 'delight')
    h2.add('diligent', 'idle')
    h2.add('guide', 'follow')
    h2.add('flow', 'jam')

    assert  left_join(h1,h2) == [ ['fond', 'enamored', 'averse'], ['outfit', 'garb', None], ['diligent', 'employed', 'idle'], ['wrath', 'anger', 'delight'], ['guide', 'usher', 'follow']]

def test_left_join_1st_empty():
    h1 = Hashtable(1024)
    h2 = Hashtable(1024)
    h2.add('fond', 'averse')
    h2.add('wrath', 'delight')
    h2.add('diligent', 'idle')
    h2.add('guide', 'follow')
    h2.add('flow', 'jam')

    assert left_join(h1,h2) == []

def test_left_join_no_matches():
    one = Hashtable(1024)
    one.add('pond','enamored')        
    one.add('rath', 'anger')          
    one.add('adiligent', 'employed')    
    one.add('poutfit', 'garb')           
    one.add('hangguide', 'usher')           

    two = Hashtable(1024)
    two.add('fond', 'averse')
    two.add('wrath', 'delight')
    two.add('diligent', 'idle')
    two.add('guide', 'follow')
    two.add('flow', 'jam')

    assert left_join(one,two) == [['rath', 'anger', None], ['pond', 'enamored', None], ['hangguide', 'usher', None], ['adiligent', 'employed', None], ['poutfit', 'garb', None]] 



