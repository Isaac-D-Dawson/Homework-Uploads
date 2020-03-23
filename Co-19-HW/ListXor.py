#ListXor.py     23.03.2020

def list_xor(n, list1, list2):
    output = False
    if n in list1 or n in list2:
        output = True
    if n in list1 and n in list2:
        output = False
    return(output)

test1 = [1,2,3,4]
test2 = [4,5,6,7]

print(list_xor(1, test1, test2))
print(list_xor(7, test1, test2))
print(list_xor(4, test1, test2))
