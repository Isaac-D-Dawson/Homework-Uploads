# Joe Palooka has fat fingers, so he always hits the “Caps Lock” key whenever he actually intends to hit the key “a” by itself. (When Joe tries to type in some accented version of “a” that needs more keystrokes to conjure the accents, he is more careful in the presence of such raffinated characters ([Shift] + [Char]) and will press the keys correctly.) Compute and return the result of having Joe type in the given text. The “Caps Lock” key affects only the letter keys from “a” to “z” , and has no effect on the other keys or characters. “Caps Lock” key is assumed to be initially off.

# Input: A string. The typed text.

# Output: A string. The showed text after being typed.

# The mission was taken from Python CCPS 109 Fall 2018. It is taught for Ryerson Chang School of Continuing Education by Ilkka Kokkarinen

#This program is technically functional but does not pass the checksum

def caps_lock(text: str) -> str:
    
    #Create local variables:
    inval = text.split("a")
    outval = ""
    
    for i in inval:
        if inval.index(i) % 2 != 0:
            outval = f"{outval}{i.swapcase()}"
        else:
            outval = f"{outval}{i}"
    
    #Had to google to confirm existence of "Swapcase".
    #found on stackoverflow at:
    #https://stackoverflow.com/a/26386127
    
    print(outval)#debug output
    return(outval)
    
if __name__ == '__main__':
    print("Example:")
    print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    print("Coding complete? Click 'Check' to earn cool rewards!")
