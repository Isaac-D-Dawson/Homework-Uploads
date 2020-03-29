#DoubleLetters.py       19.03.2020

#Define a function and make it take in strings.
def double_letters(string):
    #Set the default output to False
    output = False
    #Go through every letter in the input, except fort he last one...
    for i in range(len(string)-1):
        #...and compare it to the next letter in the string.
        if string[i] == string[i+1]:
            #if at any point two letters in order match, set the output to true, as there are repeat letters.
            output = True
    #Once you've checked everything, return the output.
    return(output)

print(double_letters("Hello"))      #true, ll
print(double_letters("HelLo"))      #false lL (Doesn't compare upper and klower case letters, but i can fix that.
print(double_letters("IIIOOOO"))    #true, despite the multiple repeats
print(double_letters("I"))          #false, you can't match anything less than two in a row.
