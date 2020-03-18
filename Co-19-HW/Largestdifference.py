#Largestdifference.py       18.03.2020

def largest_difference(list):
    smallest = list[0]
    largest = list[0]
    for i in range(1, len(list)):
        if list[i] > largest:
            largest = list[i]
        if list[i] < smallest:
            smallest = list[i]
    output = largest - smallest
    return(output)

print(largest_difference([1, 2, 3]))
print(largest_difference([-100, 11, 234, 11, 355, 400, 33, 2, 0, 00]))
print(largest_difference([1]))