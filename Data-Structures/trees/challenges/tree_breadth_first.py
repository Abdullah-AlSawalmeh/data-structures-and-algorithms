from queue import Queue
from trees.trees import *

def breadth_first(tree):
    my_tree = []
    current = tree.root
    my_queue = Queue()
    my_queue.put(current)
    while True:
        dequeued = my_queue.get()
        my_tree.append(dequeued.value)
        if dequeued.left != None:
            my_queue.put(dequeued.left)
        if dequeued.right != None:
            my_queue.put(dequeued.right)
        if my_queue.empty() == True:
            break
    return my_tree
    


if __name__ == "__main__":
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
    print(breadth_first(tree))
