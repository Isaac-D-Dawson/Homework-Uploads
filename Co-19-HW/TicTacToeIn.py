#TicTacToeIn.py     18.03.2020

#Define out function and make it take a string as input.
def get_row_col(string):
    #define a list containing the alphabet up to "I". It's a unique way of printing a list.
    alphabet = "A,B,C,D,E,F,G,H,I".split(",") #stop at I as any letters greater cause it to return too large a result.
    #Could fix, but outside the scope of this project rn.
    #Det the output as the second char of the string taken in, in upper case.
    output = int(string.upper()[1])-1
    #Then overwrite the output with a string containing the previous result, a comma, and then the first letter in the string.
    output = f"{output}{alphabet.index(string.upper()[0])}"
    #We get the numberic value of this letter by upper casing it and comparing it to our alphabet.
    #finally, return the string as a tuple, a list with two items that cannot be changed.
    return(tuple(output))

#Test calls
print(get_row_col("A3"))    #Returns "('2', '0')"
print(get_row_col("I9"))    #Returns "('8', '8')" This is the highest value the program can take, without returning a faulty result.