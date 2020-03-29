#ListXor.py     23.03.2020

#Define our function and make it take in an item and two lists
def list_xor(n, list1, list2):
    #Allocate the output and set it to False.
    output = False
    #if the item is in either list, set the output to true...
    if n in list1 or n in list2:
        output = True
        #...BUT if it;s in both lists set the output to false.
    if n in list1 and n in list2:
        output = False
    #Then return the output,
    return(output)

#Some test values,
test1 = [1,2,3,4]
test2 = [4,5,6,7]
#And test calls.
print(list_xor(1, test1, test2))    #returns True, as 1 only appears in one list.
print(list_xor(7, test1, test2))    #Returns True, as 7 only appears in one list.
print(list_xor(4, test1, test2))    #Returns False, as 4 appears in both our lists.
