#ListFlatten.py     18.03.2020

#Define our function and make it take in a list.
def flatten(list):
    #allocate the output as a list.
    output = []
    #Cycle through everything in the list...
    for i in range(len(list)):
        #And adds it to the output.
        output.extend(list[i])
    #Return the output list.
    return(output)

#Test call
print(flatten([[1,2,3,], [4,5,3], [22,3,1,6]])) #Returns "[1,2,3,4,5,3,22,3,1,6]"