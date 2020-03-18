#AddAndRemovedots.py        18.03.2020

def add_dots(string):
    output = ""
    for i in range(len(string)):
        output = f"{output}{string[i]}."
    return(output)

print(add_dots("Test"))

def remove_dots(string):
    output = ""
    for i in range(len(string)):
        if string[i] != ".":
            output = f"{output}{string[i]}"
    return(output)s

print(remove_dots("T.e.s.t."))
print(remove_dots(add_dots("Sample text!")))