#EvenFib.py     22.03.2020, finished 23.03.2020

def fib():
    fib_sequence = [1, 1]
    for i in range(0, 999): #run 1000 times, since we're starting with a zeroth and first term.
        #I'd run it 4 million times, but my computer has crashed enough today.
        fib_sequence.append(fib_sequence[-1]+fib_sequence[-2])
    return(fib_sequence)

def even(seq):
    output = 0
    for i in seq:
        if i%2 == 0:
            output += i
    return(output)

print(even(fib()))