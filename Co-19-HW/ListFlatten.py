#ListFlatten.py     18.03.2020

def flatten(list):
    output = []
    for i in range(len(list)):
        output.extend(list[i])
    return(output)

print(flatten([[1,2,3,], [4,5,3], [22,3,1,6]]))