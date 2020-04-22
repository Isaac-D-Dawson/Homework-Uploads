# In a given word you need to check if one symbol goes right after another.

# Cases you should expect while solving this challenge:

# one of the symbols are not in the given word - your function should return False;
# any symbol appears in a word more than once - use only the first one;
# two symbols are the same - your function should return False;
# the condition is case sensitive, which mease 'a' and 'A' are two different symbols.
# Input: Three arguments. The first one is a given string, second is a symbol that shoud go first, and the third is a symbold that should go after the first one.

# Output: A bool.

def goes_after(word: str, first: str, second: str) -> bool:
    
    #declare local variables:
    output = False
    
    #Sanity check: make sure both letters are in the input.
    if first in word and second in word:
        #Next, we want to find the letters.
        firstindex = word.index(first)
        secondindex = word.index(second)
        #Then, check if the two are adjacent
        if firstindex+1 == secondindex:
            output = True
    
    #Note to self: ran into a logic issue. i was comparing the first occurance of the first letter tot he next char.
    #I was in fact supposed to be comparing the first occurance of both and thrist and second letters to eachother.
    #I have since corrected for this.
    
    return output
    
# if __name__ == '__main__':
#     print("Example:")
#     print(goes_after('world', 'w', 'o'))

#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert goes_after('world', 'w', 'o') == True
#     assert goes_after('world', 'l', 'o') == False
#     assert goes_after('panorama', 'a', 'n') == True
#     assert goes_after('list', 'l', 'o') == False
#     assert goes_after('', 'l', 'o') == False
#     assert goes_after('list', 'l', 'l') == False
#     print("Coding complete? Click 'Check' to earn cool rewards!")