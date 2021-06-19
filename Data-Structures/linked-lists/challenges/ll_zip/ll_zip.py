from linked_list.linked_list import LinkedList


def zipLists(LL1,LL2):
    # print(LL1)
    # print(LL2)
    # print(LL2.head.value)
    # print(LL1.head.next.value)
    # pointer1 = LL1.head.next
    # pointer2 = LL2.head.next
    # LL1.head.next = LL2.head
    # current = LL1.head.next
    # LL1.head.next.next = pointer1
    # pointer1 = LL1.head.next.next.next
    # LL1.head.next.next.next = pointer2
    # pointer2 = LL1.head.next.next.next.next
    # LL1.head.next.next.next.next = pointer1
    # pointer1 = LL1.head.next.next.next.next.next
    # LL1.head.next.next.next.next.next = pointer2
    # pointer2 = LL1.head.next.next.next.next.next.next
    # LL1.head.next.next.next.next.next.next = pointer1
    # pointer1 = LL1.head.next.next.next.next.next.next.next
    # LL1.head.next.next.next.next.next.next.next = pointer2

    # LL1.head.next = LL2.head
    # current = LL1.head.next
    # current.next = pointer1
    # current = current.next
    # pointer1 = current.next
    # current.next = pointer2
    # current = current.next
    # pointer2 = current.next
    # current.next = pointer1
    # current = current.next
    # pointer1 = current.next
    # current.next = pointer2
    # current = current.next
    # pointer2 = current.next
    # current.next = pointer1
    # current = current.next
    # pointer1 = current.next
    # current.next = pointer2
    # current = current.next
    if LL1.head and LL2.head:
        pointer1 = LL1.head.next
        pointer2 = LL2.head.next
        LL1.head.next = LL2.head

        current = LL1.head.next
        while(current.next and pointer1 and pointer2):
            current.next = pointer1
            current = current.next
            pointer1 = current.next
            current.next = pointer2
            current = current.next
            pointer2 = current.next
        
        while(pointer1):
            current.next = pointer1 
            current = current.next
            pointer1 = current.next

        while(pointer2):
            current.next = pointer2 
            current = current.next
            pointer2 = current.next

        return LL1
    else:
        if LL1.head:
            print("Fill the second LL")
            return LL1
        elif LL2.head:
            print("Fill the first LL")
            return LL2
        else:
            print("Fill both LLs")
            return None


if __name__ == "__main__":
    LL1 = LinkedList()
    LL1.append(1)
    # LL1.append(3)
    # LL1.append(5)
    # LL1.append(7)
    # LL1.append(1)
    # LL1.append(3)

    LL2 = LinkedList()
    # LL2.append(2)
    # LL2.append(4)
    # LL2.append(6)
    # LL2.append(8)
    # LL1.append(11)
    # LL1.append(12)
    # LL1.append(15)
#     LL2.append(5)
#     LL2.append(9)
# 
#     LL1.append(2)
    # LL2.append(4)

    print(zipLists(LL1,LL2))
