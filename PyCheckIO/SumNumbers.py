# In a given text you need to sum the numbers. Only separated numbers should be counted. If a number is part of a word it shouldn't be counted.

# The text consists from numbers, spaces and english letters

# Input: A string.

# Output: An int.

def sum_numbers(text: str) -> int:

    #define environment variables:
    output = 0
    alphabet = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(",")
    
    #divide and conquer
    inval = text.lower().split(" ") #Make all the letters lowercase, and split every word.
    
    #Strip out blank entries.
    for i in inval:
        if i == "":
            inval.pop(inval.index(i))
    
    for i in inval:
        valid = True
        for j in alphabet:
            if j in i:
                valid = False
        if valid == True:
            output += int(i)
    print(output)
    return(output)

# if __name__ == '__main__':
#     print("Example:")
#     print(sum_numbers('hi'))

#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert sum_numbers('hi') == 0
#     assert sum_numbers('who is 1st here') == 0
#     assert sum_numbers('my numbers is 2') == 2
#     assert sum_numbers('This picture is an oil on canvas '
#  'painting by Danish artist Anna '
#  'Petersen between 1845 and 1910 year') == 3755
#     assert sum_numbers('5 plus 6 is') == 11
#     assert sum_numbers('') == 0
#     print("Coding complete? Click 'Check' to earn cool rewards!")
