#Palindrome.py      18.03.2020, finished on 22.03.2020

#Define our function and make it take a string.
def palindrome(string):
    #Save a reversed copy of the string as a list.
    gnirts = [i for i in reversed(list(string))]
    # print(gnirts)         Test code, to make sure the right thing was being returned
    # print(list(string))   More test code, same as above
    #if the reversed copy is the same as the non-reversed copy...
    if gnirts == list(string):
        #Return true.
        return(True)
        #Otherwise...
    else:
        #Return False.
        return(False)

#Test code
print(palindrome("bob"))    #Returns True, bob is the same forwards and backwards
print(palindrome("alice"))  #Returns False, Alice is not the same forwards and backwards.
print(palindrome("Aea"))    #Returns False,  the code is case sensitive, and A and a are different letters.
print(palindrome("aea"))    #Returns True, "aea" is the same forwards and backwards.
