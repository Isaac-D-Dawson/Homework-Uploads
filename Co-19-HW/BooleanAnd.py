#BooleanAnd.py      22.03.2020

def triple_and(a,b,c):
    result = True
    for i in [a, b, c]:
        if i != True:
            result = False
    return(result)

print(triple_and(1,1,1))
print(triple_and(1,2,3))
print(triple_and(1 == 2, 1 == 1, 1 == 1))
print(triple_and(2 == 2, 2 == 2, 2 == 2))
