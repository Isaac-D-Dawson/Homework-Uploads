from typing import List

def sort_by_ext(files: List[str]) -> List[str]:
    
    inval = [i for i in files]
    outval = []
    
    for i in inval:
        outval.append([i.split(".")[0:-1], i.split(".")[-1]])
    
    
    
    inval = [i for i in outval]
    #print(inval)
    #print(sorted(inval))
    
    for i in range(0, len(inval)):
        if inval[i][0][0] == "":
            inval[i][0][0] = f".{inval[i][1]}"
            inval[i][1] = ""
        if len(inval[i][0]) > 1:
            inval[i][0] = f"{f'{j}.' for j in inval[i][0]}"[0:-1]
    
    print(inval)
    print(sorted(inval))
            
    
    outval = []
    for i in sorted(inval, key = lambda x: x[1]):
        if i[1] == "":
            if len(i[0][0]) == 1:
                outval.append(f"{i[0][0]}.")
            else:
                outval.append(f"{i[0][0]}")
        else:
            outval.append(f"{i[0][0]}.{i[1]}")
    
    print(outval)
    return(outval)
    
if __name__ == '__main__':
    print("Example:")
    print(sort_by_ext(['1.cad', '1.bat', '1.aa']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']
    print("Coding complete? Click 'Check' to earn cool rewards!")
