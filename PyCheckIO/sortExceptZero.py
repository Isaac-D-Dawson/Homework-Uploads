# Sort the numbers in an array. But the position of zeros should not be changed.

# Input: A List.

# Output: An Iterable (tuple, list, iterator ...).

from typing import Iterable


def except_zero(items: list) -> Iterable:
    
    #Local variables:
    zeroes = []
    outval = []
    
    #Cycle through everything in our input
    for i in range(0, len(items)):#We're using a range here to make sure we get the exact index.
        if items[i] == 0:
            zeroes.append(i)   #Keep track of where this is.
        else:
            outval.append(items[i]) #Save all the non-zero numbers
    
    outval.sort()#Sort the output, duh.
    
    for i in zeroes:
        outval.insert(i, 0)#Stick all the zeroes back in where they were.
    
    #Debug calls to make sure we're getting something sane.
    #print(zeroes)
    #print(outval)
    return(outval)
    
# if __name__ == '__main__':
#     print("Example:")
#     print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
#     assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
#     assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
#     assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
#     assert list(except_zero([0, 0])) == [0, 0]
#     print("Coding complete? Click 'Check' to earn cool rewards!")
