#MultiplesOf3And5.py        22.03.2020

def fizzbuzz():
    nums = []
    for i in range(0, 1001):
        if i%3 == 0 and i%5 == 00:
            nums.append(i)
    output = 0
    for i in nums:
        output += i
    return(output)

print(fizzbuzz())