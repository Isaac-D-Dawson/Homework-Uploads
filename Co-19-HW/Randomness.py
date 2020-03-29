#Randomness.py      18.03.2020

#Define our function. It doesn't need an input though.
def random_number():
    #Import te time module so we can use functions.
    import time
    #Define our random value. This is based off of the current computer clock time.
    rand = str(time.monotonic())
    #if the last two characters are "00", return 100
    if rand[-2:] == "00":
        return("100")
    #Otherwise, Return the last two digits of rand.
    else:
        return(rand[-2:])

#Test call, returns a "random" number.
print(random_number())
#The catch is, the number it returns is dependant on the time, 
# so it can return the same number several times in a row, 
# consistently it depedns how fast it's being called and how long an interval.