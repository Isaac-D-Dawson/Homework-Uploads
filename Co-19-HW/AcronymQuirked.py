#Acronym.py     23.03.2020

def acronym(string):
    targets = string.split(" ")
    output = ""
    for i in targets:
        if len(i) > 3:
            output = output + i[0].lower()
        else:
            output = output + i[0].upper()
    return(output)

print(acronym("This is a long string"))
print(acronym("I hope it's not an issue"))
