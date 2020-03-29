#MiddleLetter.py        28.03.2020

#Define out function and make it take in a string.
def mid(string):
    #Save the length of the string.
    length = len(str(string))
    #if the string is an odd number of chars long...
    if length % 2 != 0:
        #There is a middle letter, and we can save the midpoint.
        midpoint = int((length/2)+1)
        #And we return the letter at the midpoint.
        return(str(string[midpoint]))
    #Otherwise...
    else:
        #Return blank. there is no midpoint to the string, and thus no middle letter to return
        return("")

#Test calls.
print(mid("aaa"))       #Returns "a", the middle letter.
print(mid("aaaa"))      #Retuns "", as there is no middle letter.
print(mid("isaac"))     #Returns "a", the middle letter.