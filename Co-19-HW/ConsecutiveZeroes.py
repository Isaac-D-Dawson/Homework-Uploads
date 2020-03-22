#ConsecutiveZeroes.py       22.03.2020

def consecutive_zeroes(string):
    highest = 0
    consecutive = 0
    for i in string:
        if i == "0":
            consecutive += 1
            if consecutive > highest:
                highest = consecutive
        else:
            consecutive = 0

    return(highest)

print(consecutive_zeroes("1001101000110"))