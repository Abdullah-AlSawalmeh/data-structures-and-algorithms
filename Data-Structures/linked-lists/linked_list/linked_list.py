class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is None:
            return("Linked list is empty!")
        else:
            returned = ''
            current = self.head
            while current is not None:
                    returned = returned + f'{{ { current.value } }} -> '
                    current = current.next
            else: 
                    returned = returned + 'Null'
        return returned
    
    def insert(self,value):
        """
        Adds a node of a value to the begining of LL
        """
        node = Node(value)
        node.next = self.head
        self.head = node

    def append(self,value):
        """
        Adds a node of a value to the end of LL
        """
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def includes(self,data):
        """
        Checks if the value exist in the LL or not.
        retruns : True if it is there 
                  False if not
        """
        if self.head is None:
            return False
        else:
            returned = False
            current = self.head
            while current is not None:
                if current.value == data:
                    # print(current.value)
                    returned = True
                    break
                else:
                    current = current.next
        return returned

if __name__ == "__main__":
    LL = LinkedList()
    print(LL)
    LL.append(4)
    LL.append(5)
    LL.append(6)
    LL.insert(3)
    LL.insert(2)
    LL.insert(1)
    print(LL)
    print(LL.includes(4))
    # print(str(LL))