class Node: 
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return "Tree is instantiated successfully"

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.pre_order(self.root, "")
        elif traversal_type == "inorder":
            return self.in_order(self.root, "")
        elif traversal_type == "postorder":
            return self.post_order(self.root, "")
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def pre_order(self, start ,output):
        try:
            if start:
                output += f"{str(start.value)}  "
                output = self.pre_order(start.left,output)
                output = self.pre_order(start.right,output)
            return output
        except:
            print("There is an error")

    def in_order(self, start ,output):
        try:
            if start:
                output = self.in_order(start.left,output)
                output += f"{str(start.value)}  "
                output = self.in_order(start.right,output)
            return output
        except:
            print("There is an error")

    def post_order(self, start ,output):
        try:
            if start:
                output = self.post_order(start.left,output)
                output = self.post_order(start.right,output)
                output += f"{str(start.value)}  "
            return output
        except:
            print("There is an error")

class BinarySearchTree(BinaryTree):
    def Add(self,value):
        try:
            if self.root == None:
                self.root = Node(value)
            global current 
            current = self.root
            while current :
                if value == current.value:
                    print("The value is in the tree") 
                    return True
                if value > current.value:
                    temp = current
                    current = current.right
                    if current == None:
                        temp.right = Node(value)
                        break
                if value < current.value:
                    temp = current
                    current = current.left
                    if current == None:
                        temp.left = Node(value)
                        break
        except:
            print("There is an error")


    def Contains(self,value):
        try:
            global current 
            current = self.root
            while current :
                if value == current.value:
                    print("The value is in the tree") 
                    return True
                elif value > current.value:
                    current = current.right
                
                elif value < current.value:
                    current = current.left
                
            return False
        except:
            print("There is an error")

    def find_maximum_value():
        pass





if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.Add(5)
    tree.Add(10)
    tree.Add(4)
    tree.Add(2)
    tree.Add(3)
    tree.Add(20)

    print(tree.print_tree("inorder"))
    print(tree.Contains(3))