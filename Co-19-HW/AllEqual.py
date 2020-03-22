#AllEqual.py        22.03.2020

def all_equal(list):
    check = list[0]
    result = True
    for i in range(0, len(list)):
        if list[i] != check:
            result = False
    return(result)

print(all_equal([1]))
print(all_equal([1,1,1]))
print(all_equal([1,2,1,1]))
print(all_equal([1,2,3,4,5]))
