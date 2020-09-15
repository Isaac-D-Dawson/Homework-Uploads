import Stacks

def is_match(left, right):
    outval = False
    if left == "{" and right == "}":
        outval = True
    elif left == "[" and right == "]":
        outval = True
    elif left == "(" and right == ")":
        outval = True
    return outval

def is_paren_balanced(paren_string):
    
    if paren_string == "":
        return True #an empty string is balanced
    else:   
        s           = Stack()
        is_balanced = True
        index = 0
        while index < len(paren_string):
            paren = paren_string[index]
            if paren in "({[":
                s.push(paren)
            elif not is_match(s.pop, paren):
                is_balanced = False
            index += 1
        return is_balanced


# def is_paren_balanced(paren_string):
#     s = Stack()
#     is_balanced = True
#     index = 0

#     while index < len(paren_string) and is_balanced:
#         paren = paren_string[index]
#         if paren in "([{":
#             s.push(paren)
#         elif s.is_empty:
#             is_balanced = False
#         elif not is_match(s.pop, paren):
#             is_balanced = False
#         index += 1
#     if s.is_empty and is_balanced:
#         return True
#     else:
#         return False


assert is_paren_balanced("()")      == True
assert is_paren_balanced("[][]")    == True
assert is_paren_balanced("{{}}")    == True
assert is_paren_balanced("")        == True
assert is_paren_balanced("[()]")    == True
assert is_paren_balanced("[(])")    == False
assert is_paren_balanced(")")       == False