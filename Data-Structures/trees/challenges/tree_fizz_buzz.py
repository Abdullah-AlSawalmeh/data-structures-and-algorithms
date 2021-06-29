class  k_ary_tree:
    def __init__(self, data):
        self.data = str(data)
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def tree_fizz_buzz(tree):
    spaces = ' ' * tree.get_level() * 3
    prefix = spaces + "|__" if tree.parent else ""
    print(prefix + tree.data)
    if tree.children:
        for child in tree.children:
            if int(child.data) % 5 == 0 and int(child.data) % 3 == 0 :
                child.data = "FizzBuzz"
            elif int(child.data) % 5 == 0:
                child.data = "Buzz"
            elif int(child.data) % 3 == 0:
                child.data = "Fizz"
            tree_fizz_buzz(child)
    return tree



if __name__ == "__main__":
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

    # root.print_tree()
    tree_fizz_buzz(tree)
    # print(tree.children[0].children[0].data)
    print(tree.children[1].data)