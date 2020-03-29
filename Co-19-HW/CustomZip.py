#CustomZip.py       23.03.2020

#Define our function, and allow it to take two functions, ideally iterables.
def zap(a, b):
    #Assign an output list.
    out = []
    #iterate through everything in a.
    for i in range(len(a)):
        #and append it to the output, along with an item from B with the same index.
        out.append(tuple([a[i], b[i]]))
    #And when you're finished, return the output.
    return(out)

#Test calls
print(zap([1,2,3,4],["a","b","c","d"])) #Test for logic, Returns a tuple of the two lists.
print(zap([],[]))   #Test to see if it handles emopty strings.
#Note the strings have to be the same length. at best they'll return short, at worst, they'll crash with an indexing error.