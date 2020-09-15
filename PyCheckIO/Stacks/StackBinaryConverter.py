import Stacks

def bin_convert(number):
    s = Stacks.Stack()
    while number > 0:
        s.push(number%2)
        number = number//2
    
    outval = ""
    while not s.is_empty:
        outval += str(s.pop)
    
    return outval

assert bin_convert(15)  == "1111"
assert bin_convert(16)  == "10000"
assert bin_convert(500) == "111110100"