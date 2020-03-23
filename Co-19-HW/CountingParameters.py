#CountingParameters.py      23.03.2020

def param_count(*args):
    return(len(args))

print(param_count(1,2,3,4))
print(param_count())
print(param_count(1))
