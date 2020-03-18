#CapitalIndexes/py      18.03.2020

def capital_indexes(string):
    lowerString = string.lower()
    output = []
    for i in range(len(string)):
        if string[i] != lowerString[i]:
            output.append(i)
    return(output)

print(capital_indexes("HeLlO"))
print(capital_indexes("HELLo"))
print(capital_indexes("Hi World!"))
