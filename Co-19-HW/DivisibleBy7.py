#DivisibleBy7.py        23.03.2020

def divBySeven(rang):
    output = ""
    for i in rang:
        if i % 7 == 0 and i % 5 != 0:
            output = output + f"{i}, "
    return(output)

print(divBySeven(range(2000, 3201)))