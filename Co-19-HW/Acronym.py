#Acronym.py     23.03.2020

#Define function "Acronym" which takes in a single string.
def acronym(string):
    #Define a variable to help check if a letter is the first in a word
    first_tag = False
    #Save the first letter of the string, capitalised.
    output = string[0].upper()
    #For every letter in the string except the first one...
    for i in range(1, len(string)):
        #if a letter in the string is a space...
        if string[i] == " ":
            #...Then the next one is the first in a word...
            first_tag = True
            #....and if it's the first letter...
        elif first_tag == True:
            #...Save it, capitalised, to our output.
            output = output + string[i].upper()
            #And reset to make sure we don't keep identifying.
            first_tag = False
        #And once we've done that for all the letters in the string, return it.
    return(output)

#Test calls:
print(acronym("This is a long string")) #TIALS
print(acronym("I hope it's not an issue")) #iHINAS