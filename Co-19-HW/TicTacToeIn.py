#TicTacToeIn.py     18.03.2020

def get_row_col(string):
    alphabet = "A,B,C,D,E,F,G,H,I".split(",") #stop at I as any letters greater cause it to return too large a result.
    #Could fix, but outside the scope of this project rn.
    output = int(string.upper()[1])-1
    output = f"{output}{alphabet.index(string.upper()[0])}"
    return(tuple(output))

print(get_row_col("A3"))
print(get_row_col("I9")) # highest value