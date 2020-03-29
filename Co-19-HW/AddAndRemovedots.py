#AddAndRemovedots.py        18.03.2020

#define the add_dots function, and make it take in a string input.
def add_dots(string):
    #declare the output.
    output = ""
    #for every letter in the string...
    for i in range(len(string)):
        #add it to the output with a "."
        output = f"{output}{string[i]}."
    #And return it to the caller when you're finished.
    return(output)

#Call the funtion to test it.
print(add_dots("Test")) #returns "Y.e.s.t."

#Define the remove_dots function, and have it take in a string.
def remove_dots(string):
    #declare the output for later.
    output = ""
    #for every char in the string...
    for i in range(len(string)):
        #...check if it;s a dot...
        if string[i] != ".":
            #and if it isn't, add it to the output.
            output = f"{output}{string[i]}"
        #when you've done all that, return the output.
    return(output)s

#Test calls.
print(remove_dots("T.e.s.t.")) #Returns "Test"
print(remove_dots(add_dots("Sample text!")))# The two functions cancel out, so it returns "Sample text!"