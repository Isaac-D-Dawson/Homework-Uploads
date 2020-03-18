#TypeCheck.py       18.0.2020

#Vibe Check:

def only_ints(val1, val2):
    if isinstance(val1, int) == True and isinstance(val2, int) == True:
        return(True)
    else:
        return(False)

print(only_ints("a", 1))
print(only_ints("b", 2))
print(only_ints("2", "1"))
print(only_ints("no", "true"))
print(only_ints(5, 20))