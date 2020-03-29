#Syllablecounter.py        23.03.2020

#Define out function and make it take a string as input.
def count(string):
    #Allocate a variable "hyphens" and set it to 0.
    hyphens = 0
    #Check every letter in the string...
    for i in string:
        #...to see if it's a hyphen.
        if i == "-":
            #And if it is, add it to the output.
            hyphens += 1
    #After that, return the number of hypgens, plus one.
    return(hyphens+1)

#Test calls
print(count("ho-tel"))      #Returns 2.
print(count("tri-va-go"))   #Returns 3.
print(count("cat"))         #Returns 1.
print(count("met-a-phor"))  #Returns 3.
print(count("ter-min-a-tor"))   #Returns 4.
print(count("ex-term-in-ate"))  #Returns 4.
