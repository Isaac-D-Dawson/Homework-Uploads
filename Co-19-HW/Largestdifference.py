#Largestdifference.py       18.03.2020

#Define our function and make it take in a list.
def largest_difference(list):
    #define the smallest value as the first item in the list
    smallest = list[0]
    #And also set the largest as the first value in the list.
    largest = list[0]
    #Then cycle through every item in the list.
    for i in range(1, len(list)):
        #if it's bigger than the largest...
        if list[i] > largest:
            #...Save it as the largest.
            largest = list[i]
        #And if it's smaller than the smallest...
        if list[i] < smallest:
            #...save it as the smallest.
            smallest = list[i]
    #When you're done, save the difference between the largest and smallest as the output.
    output = largest - smallest
    #Finally, we return the output.
    return(output)

#Test calls.
print(largest_difference([1, 2, 3]))    #Returns 2(3-1)
print(largest_difference([-100, 11, 234, 11, 355, 400, 33, 2, 0, 00]))  #Returns 500 (400--100)
print(largest_difference([1]))  #Returns 0. There's no difference between one and itself.