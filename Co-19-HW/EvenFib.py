#EvenFib.py     22.03.2020, finished 23.03.2020

#Define out function. it doesn't need to take any inputs.
def fib():
    #Define a list that stores the fibionacci sequence, containing the 0th and first terms.
    fib_sequence = [1, 1]
    for i in range(0, 999): #run 1000 times, since we're starting with a zeroth and first term.
        #I'd run it 4 million times, but my computer has crashed enough today.
        #add the next term to the existing sequence by summing the previous two terms.
        fib_sequence.append(fib_sequence[-1]+fib_sequence[-2])
    #Once that's done, return the result.
    return(fib_sequence)

#Define a new function that takes in a sequence. in our case, the fibionacci sequence we made earlier.
def even(seq):
    #Set the output to 0.
    output = 0
    #And for every number in the sequence...
    for i in seq:
        #...if it's even(wholly divisible by 2)
        if i%2 == 0:
            #Add it to our output
            output += i
    #When we've done the whole sequence, Return the result.
    return(output)

#Test call.
print(even(fib())) #Should return the sub of all even numbers in the fibionacci sequence.