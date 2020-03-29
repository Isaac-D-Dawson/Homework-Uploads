#DivisibleBy7.py        23.03.2020

#Define our function that takes a range. It doesn't need to take a range, but I made it this way for conveneience.
def divBySeven(rang):
    #Allocate our output as an epty string for later.
    output = ""
    #Go though every number in the range.
    for i in rang:
        #if it divides perfectly into 7, but does not divide perfectly into five...
        if i % 7 == 0 and i % 5 != 0:
            #Add it to the output...
            output = output + f"{i}, "
    #and when you;ve finished doing that, return the results.
    return(output)

#Test call.
print(divBySeven(range(2000, 3201))) #Returns a string containing every such number from 2000 to 3200. the +1 is for the range's exclusive stop.