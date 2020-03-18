#Randomness.py      18.03.2020

def random_number():
    import time
    rand = str(time.monotonic())
    if rand[-2:] == "00":
        return("100")
    else:
        return(rand[-2:])

print(random_number())
