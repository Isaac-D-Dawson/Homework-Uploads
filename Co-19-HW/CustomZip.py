#CustomZip.py       23.03.2020

def zap(a, b):
    out = []
    for i in a:
        out.append(tuple([i, b[a.index(i)]]))
    return(out)

print(zap([1,2,3,4],["a","b","c","d"]))