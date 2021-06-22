from stacks_and_queues.stacks_and_queues import *

def is_left(bracket):
    if bracket == '(' or bracket =='[' or bracket == '{':
        return True
    else:
        return False

def is_right(bracket):
    if bracket == ')' or bracket == ']' or bracket == '}':
        return True
    else:
        return False

def opposite(bracket):
    if bracket == ')':
        return '('
    elif bracket == ']':
        return '['
    elif bracket == '}':
        return '{'

def multi_bracket_validation(input):
    bracket_stack = Stack()
    
    for i in input:
        if is_left(i):
            bracket_stack.push(i)
        if is_right(i):
            if bracket_stack.is_empty():
                return False
            else:
                if bracket_stack.top is not None:
                    if opposite(i) == bracket_stack.top.value:
                        bracket_stack.pop()

                    else:
                        return False
                else:
                    return True
    if bracket_stack.is_empty:
        return True
                


if __name__ == "__main__":
    print(multi_bracket_validation('[]()[]'))
    print(multi_bracket_validation('{}'))
    print(multi_bracket_validation('{}(){}'))
    print(multi_bracket_validation('()[[Extra Characters]]'))
    print(multi_bracket_validation('(){}[[]]'))
    print(multi_bracket_validation('{}{Code}[Fellows](())'))
    print(multi_bracket_validation('[({}]'))
    print(multi_bracket_validation('(]('))
    print(multi_bracket_validation('{(})'))
