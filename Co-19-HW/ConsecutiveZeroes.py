#ConsecutiveZeroes.py       22.03.2020

#Define our function and make it take a string as input.
def consecutive_zeroes(string):
    #Allocate a variable called Highest. We use this for comparisons later.
    highest = 0
    #Allocate another variable called Consecutive, also used for comparisons later.
    consecutive = 0
    #For ever character in the string...
    for i in string:
        #...check if it's "0"
        if i == "0":
            #Add one to consecutive...
            consecutive += 1
            #And if consecutive is more than our highest record...
            if consecutive > highest:
                #Overwrite highest to match.
                highest = consecutive
        else:
            #if it's not a "0" char, then it's not consecutive anymore, and we can drop consecutive back to 0.
            consecutive = 0
    #Finally, Return the highest result we got.
    return(highest)

#Test calls.
print(consecutive_zeroes("1001101000110"))  #Logic test. should return "3", and it does.
print(consecutive_zeroes("0"))  #Check to see how it handles 1-length strings that are valid.    Returns 1.
print(consecutive_zeroes("1"))  #Check to see how it handles 1-length strings that aren't valid. Returns 0.
print(consecutive_zeroes(""))   #Check to see how it handles 0-length strings. Returns 0 with no errors.