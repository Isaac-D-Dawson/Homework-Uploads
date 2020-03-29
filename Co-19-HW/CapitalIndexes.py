#CapitalIndexes/py      18.03.2020

#Define our function and make it take a string as input.
def capital_indexes(string):
    #make sure we have a lowercase copy of the string for checking.
    lowerString = string.lower()
    #Allocate our output list for later.
    output = []
    #Create a loop and cuc;e through every letter in the string.
    for i in range(len(string)):
        #Here we're comparing the uppercase letters and the lowercase letters.
        if string[i] != lowerString[i]:
            #if they're not equal, we save their index to the output, as they must be capital letters.
            output.append(i)
    #Then we return the output list.
    return(output)

#Test calls.
print(capital_indexes("HeLlO")) #Returns "0, 2, 4", as those chars are capitallised.
print(capital_indexes("HELLo")) #Returns "0, 1, 2, 3", as those chars are capitalised,
print(capital_indexes("Hi World!")) #Returns "0, 3", as those chars are capitalised.
