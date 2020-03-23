#ThousandsSeperator.py      23.03.2020

def format_number(num):
    mun = list(reversed(str(num)))
    offset = 0
    for i in range(3, (len(str(num))), 3):
        #print(mun) Testcode
        mun.insert(i+offset, ",")
        #print(mun) Also test code
        offset += 1
    result = list(reversed(mun))
    out = ""
    for i in result:
        out = out + i
    return(out)

print(format_number(10))
print(format_number(100))
print(format_number(1000))
print(format_number(10000))
print(format_number(100000))
print(format_number(1000000))
print(format_number(10000000))
print(format_number(100000000))
print(format_number(1000000000))
print(format_number(10000000000))
print(format_number(100000000000))
