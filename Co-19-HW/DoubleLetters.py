#DoubleLetters.py       19.03.2020

def double_letters(string):
    output = False
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            output = True
    return(output)

print(double_letters("Hello"))      #true, ll
print(double_letters("HelLo"))      #false lL (Can fix)
print(double_letters("IIIOOOO"))    #true, despite the multiple repeats
print(double_letters("I"))          #false, you can't match anything less than two in a row.
