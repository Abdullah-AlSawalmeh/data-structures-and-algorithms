from trees.trees import *

def test_empty_tree():
    ### Can successfully instantiate an empty tree
    tree = BinarySearchTree()
    tree2 = BinaryTree()
    assert str(tree) == 'Tree is instantiated successfully'
    assert str(tree2) == 'Tree is instantiated successfully'

def test_single_root_node():
    ### Can successfully instantiate a tree with a single root node
    tree = BinarySearchTree()
    tree.Add(5)
    assert tree.root.value == 5

def test_left_right_child():
    ### Can successfully add a left child and right child to a single root node
    tree = BinarySearchTree()
    tree.Add(5)
    tree.Add(10)
    tree.Add(4)
    assert tree.root.value == 5
    assert tree.root.left.value == 4
    assert tree.root.right.value == 10

def test_preorder_ineorder_posteorder_child():
    ### Can successfully return a collection from a preorder traversal
    ### Can successfully return a collection from a inorder traversal
    ### Can successfully return a collection from a postorder traversal
    tree = BinarySearchTree()
    tree.Add(5)
    tree.Add(10)
    tree.Add(4)
    assert tree.print_tree("preorder") == "5  4  10  "
    assert tree.print_tree("inorder") == "4  5  10  "
    assert tree.print_tree("postorder") == "4  10  5  "


def test_max():
    tree = BinaryTree()
    # assert tree.find_maximum_value is None
    
    tree.root = Node(2)
    tree.root.left = Node(7)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)
    tree.root.right = Node(5)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(4)
    assert tree.find_maximum_value() == 11
