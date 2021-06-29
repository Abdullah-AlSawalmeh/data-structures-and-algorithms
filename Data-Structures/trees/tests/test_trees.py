from trees.trees import *
from challenges.tree_breadth_first import *
from challenges.tree_fizz_buzz import *

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

def test_breadth_first():
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(7)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)
    tree.root.right = Node(5)
    tree.root.right.right = Node(9)
    tree.root.right.right.right = Node(5)
    tree.root.right.right.left = Node(4)
    tree.root.right.right.left.left = Node(16)
    tree.root.left.right.right.right = Node(17)
    assert breadth_first(tree) == [2, 7, 5, 2, 6, 9, 5, 11, 4, 5, 17, 16]


def test_tree_fizz_buzz():
    tree = k_ary_tree(1)

    first_branch = k_ary_tree(2)
    first_branch.add_child(k_ary_tree(3))
    first_branch.add_child(k_ary_tree(4))
    first_branch.add_child(k_ary_tree(5))

    second_branch = k_ary_tree(6)
    second_branch.add_child(k_ary_tree(7))
    second_branch.add_child(k_ary_tree(8))
    second_branch.add_child(k_ary_tree(9))

    third_branch = k_ary_tree(10)
    third_branch.add_child(k_ary_tree(11))
    third_branch.add_child(k_ary_tree(12))

    fourth_branch = k_ary_tree(15)
    fourth_branch.add_child(k_ary_tree(12))
    fourth_branch.add_child(k_ary_tree(20))

    tree.add_child(first_branch)
    tree.add_child(second_branch)
    tree.add_child(third_branch)
    tree.add_child(fourth_branch)

    assert tree.children[1].data == "6"
    assert tree.children[2].data == "10"
    assert tree.children[3].data == "15"
    assert tree.children[0].children[0].data == "3"
    assert tree.children[0].children[2].data == "5"
    assert tree.children[1].children[2].data == "9"
    assert tree.children[2].children[1].data == "12"
    assert tree.children[3].children[0].data == "12"
    assert tree.children[3].children[1].data == "20"

    tree_fizz_buzz(tree)


    assert tree.children[1].data == "Fizz"
    assert tree.children[2].data == "Buzz"
    assert tree.children[3].data == "FizzBuzz"
    assert tree.children[0].children[0].data == "Fizz"
    assert tree.children[0].children[2].data == "Buzz"
    assert tree.children[1].children[2].data == "Fizz"
    assert tree.children[2].children[1].data == "Fizz"
    assert tree.children[3].children[0].data == "Fizz"
    assert tree.children[3].children[1].data == "Buzz"