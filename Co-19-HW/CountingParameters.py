#CountingParameters.py      23.03.2020

#Define our function, and specify that it should take an unspecified number of arguments.
def param_count(*args):
    #Then count how many arguments we took in by getting the length of the list, and return that.
    return(len(args))

#Test calls
print(param_count(1,2,3,4)) #Logic check. Returns 4, as there are four arguments.
print(param_count())        #Logic check, Returns 0, as there are no arguments. This was to make sure it wouldn't error or crash.
print(param_count(1))       #Logic check, Returns 1, as there's one argument.
