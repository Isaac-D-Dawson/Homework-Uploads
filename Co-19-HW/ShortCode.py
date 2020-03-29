#ShortCode.py       22.03.2020

#Define our function and make it take a list.
def convert(list):
        #Return a list of strings, each string containing one item in the list.
        return([str(i) for i in list])

#Test Calls
print(convert([1,2,3,4]))               #Returns "["1","2","3","4"]"
print(convert(["a", "b", "c" "d"]))     #Returns "["a", "b", "c" "d"]""
print(convert([1]))                     #Returns "["1"]"
