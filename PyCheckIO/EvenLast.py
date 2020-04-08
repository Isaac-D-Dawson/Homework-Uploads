def checkio(array: list) -> int:
    """
        sums even-indexes elements and multiply at the last
    """
    
    #allocate output
    output = 0
    
    #if list isn't empty...
    if array != []:
        #For every second(even) item in the array, starting at 0.
        #make sure to actutally use the right loop syntax.
        for i in range(0, len(array), 2):
            output += array[i]
        output = output*array[-1]
    #finally, reutnr out output
    return(output)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))
    
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
