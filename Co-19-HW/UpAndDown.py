#UpAndDown.py       22.03.2020

#Define a funciton and make it take a number as input.
def up_down(num):
    #Return a tuple containing a number 1-less than the input, and one more than the input.
    return(tuple([num-1, num+1]))

#Test calls:
print(up_down(3))       #Returns "('2','4')"
print(up_down(5))       #Reutnrs "('4','6')"
print(up_down(7))       #Returns "('6','8')"
print(up_down(3.14159)) #Returns "('2.14159','4.14159')"
print(up_down(0))       #Returns "('-1','1')"
print(up_down(-5))      #Returns "('-6','-4')"
