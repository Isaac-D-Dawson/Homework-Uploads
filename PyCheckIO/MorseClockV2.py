# Help Stephen to create a module for converting a normal time string to a morse time string. As you can see in the illustration, a gray circle means on, while a white circle means off. Every digit in the time string contains a different number of slots. The first digit for the hours has a length of 2 while the second digit for the hour has a length of 4. The first digits for the minutes and seconds have a length of 3 while the second digits for the minutes and seconds have a length of 4. Every digit in the time is converted to binary representation. You will convert every on (or 1) signal to dash ("-") and every off (or 0) signal to dot (".").

# source: Wikipedia
# https://en.wikipedia.org/wiki/Binary_clock

# An time string could be in the follow formats: "hh:mm:ss", "h:m:s" or "hh:m:ss". The "missing" digits are zeroes. For example, "1:2:3" is the same as "01:02:03".

# The result will be a morse time string with specific format:
# "h h : m m : s s"
# where each digits represented as sequence of "." and "-"

# Input: A normal time string as a string (unicode).

# Output: The morse time string as a string.

# Precondition:
# time_string contains correct time.


# CHANGELOG:
# V 2.0:
# -Reworked the list append calls into a function:
# =function returns strings rather than working with a list:
# =This is because no list functions were being used
# =This also removes the need for an additional formatting loop
# =Function is ducktyped and uses an optional keyword argument:
# =-This reduces the number of inputs assigned each call
# V 1.0:
# -Program created:
# =Program uses list append statements and a formatting loop to generate the output


def checkio(time_string: str) -> str:
    
    inval = time_string.split(":")
    outval = ""
    
    for i in range(0, len(inval)):
        if len(inval[i]) < 2:
            inval[i] = f"0{inval[i]}"
    
    #The easiets way to do this is jsut a clunky 1-1 conversion...
    #...but since they don;t give us a list, we have to write out the thing outrselves >.<
    morseNumbers = ["....", "...-", "..-.", "..--", ".-..", ".-.-", ".--.", ".---", "-...", "-..-"]
    
    #Keep in mind, what this code actually wants is for us to translate the time into *Binary* and then represent that in morse....
    
    def encode(unit: int, digit: int, kwarg: int = 0) -> str:
        kwarg
        return(f"{outval}{morseNumbers[int(inval[unit][digit])][kwarg:]} ")
    
    outval = encode(0, 0, -2)      #H
    outval = encode(0, 1)          #H
    outval = f"{outval}: "
    outval = encode(1, 0, -3)      #M
    outval = encode(1, 1)          #M
    outval = f"{outval}: "
    outval = encode(2, 0, -3)      #S
    outval = encode(2, 1)          #S

    #There is a pattern here, however it's very hard to loop.
    
    print(outval[0:-1]) #The "[0:-1]" is to trim the trailing space
    return(outval[0:-1])
    
if __name__ == '__main__':
    print("Example:")
    print(checkio("10:37:49"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
    print("Coding complete? Click 'Check' to earn cool rewards!")
