#MiddleLetter.py        28.03.2020

def mid(string):
    length = len(str(string))
    if length % 2 != 0:
        midpoint = int((length/2)+1)
        return(str(string[midpoint]))
    else:
        return("")

print(mid("aaa"))
print(mid("aaaa"))
print(mid("isaac"))