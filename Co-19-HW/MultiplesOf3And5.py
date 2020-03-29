#MultiplesOf3And5.py        22.03.2020

#Define out function. It doesn't need any inputs. I chose fizzbuss as the name as it felt right.
def fizzbuzz():
    #Allocate a list called nums.
    nums = []
    #Cycle through every number from 1 to 1000.
    for i in range(0, 1001):
        #If that number is wholly divisible by both three and five...
        if i%3 == 0 and i%5 == 0:
            #Add it to our saved nums.
            nums.append(i)
    #Define out output as 0...
    output = 0
    #...And for every number we got from the last list...
    for i in nums:
        #Add it to the output
        output += i
    #Then return the output, the sub of all multiples of 15 between 1 and 1000.
    return(output)

#Test call
print(fizzbuzz()) #Returns 33165