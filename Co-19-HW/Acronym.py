#Acronym.py     23.03.2020

def acronym(string):
    first_tag = False
    output = string[0].upper()
    for i in range(1, len(string)):
        if string[i] == " ":
            first_tag = True
        elif first_tag == True:
            output = output + string[i].upper()
            first_tag = False
    return(output)

print(acronym("This is a long string"))
print(acronym("I hope it's not an issue"))
