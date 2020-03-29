#AllEqual.py        22.03.2020

#Define our all_equal function and make it take a list.
def all_equal(list):
    #Save the first item as the check.
    check = list[0]
    #set the output to be True.
    result = True
    #For everything in the input...
    for i in range(0, len(list)):
        #...if it's not equal to the check...
        if list[i] != check:
            #...make the output false.
            result = False
            #This makes it so that if any item doesn't match the first one, it will return false, but otherwise return true.
    #When you've done that, return the result.
    return(result)

#Test calls.
print(all_equal([1])) #Vhevk to see how it handles with one input. returns True.
print(all_equal([1,1,1])) #Test to make sure logic works. Returns true.
print(all_equal([1,2,1,1])) #Test to see if logic works. Returns False, as 2 != 1
print(all_equal([1,2,3,4,5])) #Test to see if it handles everything being different. Returns false, as none of these are equal.
