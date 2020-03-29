#DivisibleBy3.py        18.03.2020

#Define a function and make it take an integer as input
def div_3(int):
    #if the number, when divided by free, doesn't return a remainder...
    if int % 3 == 0:
        #...then it's divisible by three, and we return True...
        return(True)
        #otherwise...
    else:
        #...it's not divisible by three and we return False.
        return(False)

#Test calls
print(div_3(1)) #1 isn't divisible by 3, so returns False
print(div_3(2)) #2 isn't divisible by 3, so returns False
print(div_3(3)) #3 is divisible by 3, so returns True
print(div_3(4)) #4 isn't divisible by 3, so returns False
print(div_3(5)) #5 isn't divisible by 3, so returns False
print(div_3(6)) #6 is divisible by 3, so returns True
print(div_3(7)) #7 isn't divisible by 3, so returns False
