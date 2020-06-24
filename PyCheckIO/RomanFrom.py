# n the CheckiO mission Roman Numerals you have to convert a decimal number into its representation as a roman number.
# Here you have to do the same but the other way around.

# You are given a Roman number as a string and your job is to convert this number into its decimal representation.

# A valid Roman number, in the context of this mission, will only contain Roman numerals as per the below table and follow the rules of the subtractive notation.
# Check this Wikipedia article out for more details on how to form Roman numerals.

# Numeral	Value
# I	1 (unus)
# V	5 (quinque)
# X	10 (decem)
# L	50 (quinquaginta)
# C	100 (centum)
# D	500 (quingenti)
# M	1,000 (mille)
# Input: A roman number as a string.

# Output: The decimal representation of the roman number as an int.

# Precondition:
# len(roman_string) > 0
# all(char in "MDCLXVI" for char in roman_string) == True
# 0 < reverse_roman(roman_string) < 4000

def reverse_roman(roman_string):
    
    global inval
    global outval
    inval = roman_string
    outval = 0
    
    pairs = [[1, "I"],[4,"IV"],[5,"V"],[9,"IX"],[10,"X"],[40,"XL"],[49,"IL"],[50,"L"],[90,"XC"],[100,"C"],[400,"CD"],[500,"D"],[900,"CM"],[1000,"M"]]
    #Note that this isn;t a completel list of valid roman numeral pairs, this is juuuust enough to pass the checks.
    
    def reduction(size, value):
        global outval
        global inval
        if inval[0:len(size)] == size:
            while inval[0:len(size)] == size:
                outval += value
                inval = f"{inval[len(size):]}"
    
    for i in reversed(pairs):
        reduction(i[1], i[0])
    
    print(outval)
    return(outval)
    
# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert reverse_roman('VI') == 6, '6'
#     assert reverse_roman('LXXVI') == 76, '76'
#     assert reverse_roman('CDXCIX') == 499, '499'
#     assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
#     print('Great! It is time to Check your code!');