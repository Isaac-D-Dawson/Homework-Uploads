#BooleanAnd.py      22.03.2020

#Create out function and allow it to take three inputs.
def triple_and(a,b,c):
    #Set out default output to True. if everything is fine this won't change.
    result = True
    #cycle through our inputs.
    for i in [a, b, c]:
        #See if each of our inputs are true.
        if i != True:
            #if any of them aren't, We set the output to false.
            result = False
    #Then we return the output. if anything didn't evaluate to true, then False will be returned.
    return(result)

#Test calls.
print(triple_and(1,1,1))    #Logic check. Returns True
print(triple_and(1,2,3))    #Logic check. Returns False, as each individual statement is true, but they aren;t equal.
print(triple_and(1 == 2, 1 == 1, 1 == 1))   #Logic Check. 1 doesn't equal 2, so it should return false, and it does.
print(triple_and(2 == 2, 2 == 2, 2 == 2))   #Logic check. This si tos ee if it'll parse expressions, and it does. Returns True, as 1 always equals 1.
