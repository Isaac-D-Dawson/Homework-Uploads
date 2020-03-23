#Syllablecounter        23.03.2020

def count(string):
    hyphens = 0
    for i in string:
        if i == "-":
            hyphens += 1
    return(hyphens+1)

print(count("ho-tel"))
print(count("tri-va-go"))
print(count("cat"))
print(count("met-a-phor"))
print(count("ter-min-a-tor"))
print(count("ex-term-in-ate"))
