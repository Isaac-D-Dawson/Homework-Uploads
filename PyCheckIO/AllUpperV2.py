# Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it - function should return False.

# Input: A string.

# Output: a boolean.

# Precondition: a-z, A-Z, 1-9 and spaces

def is_all_upper(text: str) -> bool:

    #Lets just initialise local vars.
    output = False
    alphabet = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(",")
    
    for i in text.lower():
        if i in alphabet:
            output = True
    if text != text.upper():
        output = False
    
    return(output)

# if __name__ == '__main__':
#     print("Example:")
#     print(is_all_upper('ALL UPPER'))

#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert is_all_upper('ALL UPPER') == True
#     assert is_all_upper('all lower') == False
#     assert is_all_upper('mixed UPPER and lower') == False
#     assert is_all_upper('') == False
#     print("Coding complete? Click 'Check' to earn cool rewards!")