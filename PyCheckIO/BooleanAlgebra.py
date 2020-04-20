# In mathematics and mathematical logic, Boolean algebra is a sub-area of algebra in which the values of the variables are true or false, typically denoted with 1 or 0 respectively. Instead of elementary algebra where the values of the variables are numbers and the main operations are addition and multiplication, the main operations of Boolean algebra are the conjunction (denoted ∧), the disjunction (denoted ∨) and the negation (denoted ¬).

# In this mission you should implement some boolean operations:
# - "conjunction" denoted x ∧ y, satisfies x ∧ y = 1 if x = y = 1 and x ∧ y = 0 otherwise.
# - "disjunction" denoted x ∨ y, satisfies x ∨ y = 0 if x = y = 0 and x ∨ y = 1 otherwise.
# - "implication" (material implication) denoted x→y and can be described as ¬ x ∨ y. If x is true then the value of x → y is taken to be that of y. But if x is false then the value of y can be ignored; however the operation must return some truth value and there are only two choices, so the return value is the one that entails less, namely true.
# - "exclusive" (exclusive or) denoted x ⊕ y and can be described as (x ∨ y)∧ ¬ (x ∧ y). It excludes the possibility of both x and y. Defined in terms of arithmetic it is addition mod 2 where 1 + 1 = 0.
# - "equivalence" denoted x ≡ y and can be described as ¬ (x ⊕ y). It's true just when x and y have the same value.
# Here you can see the truth table for these operations:

#  x | y | x∧y | x∨y | x→y | x⊕y | x≡y |
# --------------------------------------
#  0 | 0 |  0  |  0  |  1  |  0  |  1  |
#  1 | 0 |  0  |  1  |  0  |  1  |  0  |
#  0 | 1 |  0  |  1  |  1  |  1  |  0  |
#  1 | 1 |  1  |  1  |  1  |  0  |  1  |
# --------------------------------------
# You are given two boolean values x and y as 1 or 0 and you are given an operation name as described earlier. You should calculate the value and return it as 1 or 0.

# Input: Three arguments. X and Y as 0 or 1. An operation name as a string.

# Output: The result as 1 or 0.

# Precondition: x in (0, 1)
# y in (0, 1)
# operation in ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

#might be unicode translation issues with some of the headers, just in case you're wondering.
#There's probably existing boolean alegebraic operators in python, but "Every Jedi..."


OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    
    output = ""
    
    if operation == "conjunction":
        if x == y and x == 1:
            output = "1"
        else:
            output = "0"
    if operation == "disjunction":
        if x == y and x == 0:
            output = "0"
        else:
            output = "1"
    #These two specifically are remarkably similar.
    #with a bit of fiddiling I think I could use only the one "if".
    
    #This one is a little trickier.
    if operation == "implication":
        if x == 1:
            output = str(y)
        else:
            output = "1"
    
    #A bit of a cheat here, but if only two options are possible we can evade the extra steps
    if operation == "exclusive":
        if x != y:
            output = "1"
        else:
            output = "0"
        
    #This one's easy. jsut equal to.
    if operation == "equivalence":
        if x == y:
            output = "1"
        else:
            output = "0"
    
    #print(output)
    return(int(output))
    
# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert boolean(1, 0, "conjunction") == 0, "and"
#     assert boolean(1, 0, "disjunction") == 1, "or"
#     assert boolean(1, 1, "implication") == 1, "material"
#     assert boolean(0, 1, "exclusive") == 1, "xor"
#     assert boolean(0, 1, "equivalence") == 0, "same?"
#     print('All good! Go and check the mission.')
