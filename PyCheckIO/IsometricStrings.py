# Maybe it's a cipher? Maybe, but we don’t know for sure.

# Maybe you can call it "homomorphism"? i wish I know this word before.

# You need to check that the 2 given strings are isometric. This means that a character from one string can become a match for characters from another string.

# One character from one string can correspond only to one character from another string. Two or more characters of one string can correspond to one character of another string, but not vice versa.

# Input: Two arguments. Both strings.

# Output: Boolean.

# Precondition:
# both strings are the same size

def isometric_strings(str1: str, str2: str) -> bool:
    
    #allocate local variables:
    inval = []
    outval = False #Guilty until proven innocent
    
    list1 = []
    list2 = []
    
    comp1 = ""
    comp2 = ""
    
    #Grab all non-duplicate letters from the first input
    for i in str1:
        if i not in inval and i != " ": #Ignore spaces, as that might cause problems.
            inval.append(i)
    
    for i in range(0, len(inval)):#Assign each letter a unique number for comparison
        list1.append([inval[i], i])
    
    inval = []  #Reset inval real quick
    
    #Grab all non-duplicate letters from the second input
    for i in str2:
        if i not in inval and i != " ":#Alternatively we could strip out all the spaces, but that'd be more tedious.
            inval.append(i)
    
    for i in range(0, len(inval)):#Assign each letter a unique number for comparison
        list2.append([inval[i], i])
    
    #A couple of debug calls
    #print(list1)
    #print(list2)
    
    #Replace each letter in the input string with it's corresponding number
    for i in list1:
        for j in str1:
            if j == i[0]:
                comp1 = f"{comp1}{i[1]}"
    
    #Do the same thing for the second string
    for i in list2:
        for j in str2:
            if j == i[0]:
                comp2 = f"{comp2}{i[1]}"
                
    #print(comp1)
    #print(comp2)
    
    #Compare the two. if they're equal, return True
    if comp2 == comp1:
        outval = True
    
    return outval
    
# if __name__ == '__main__':
#     print("Example:")
#     print(isometric_strings('add', 'egg'))

#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert isometric_strings('add', 'egg') == True
#     assert isometric_strings('foo', 'bar') == False
#     assert isometric_strings('', '') == True
#     assert isometric_strings('all', 'all') == True
#     print("Coding complete? Click 'Check' to earn cool rewards!")
