#TypeCheck.py       18.0.2020

#Vibe Check:

#Define a function that takes in two values.
def only_ints(val1, val2):
    #Check the type of instances 1 and 2, and see if they're both equal to True.
    if isinstance(val1, int) == True and isinstance(val2, int) == True:
        #If they are, return True.
        return(True)
    else:
        #otherwise, return False
        return(False)

#Test calls.
print(only_ints("a", 1))        #Returns False, "a"  isn;t a number.
print(only_ints("b", 2))        #Returns False, "b" isn't a number.
print(only_ints("2", "1"))      #Returns False, "1" and "2" are numbers in string format.
print(only_ints("no", "true"))  #Returns False, "no" and "true" aren't numbers.
print(only_ints(5, 20))         #Returns True, Both "5" and "20" are numbers.