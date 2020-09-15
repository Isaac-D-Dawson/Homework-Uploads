factorial_cache = {0: 1, 1: 1}

def rec_fact(val: int, mult: int= 1) -> int:
    print(val)
    if val in factorial_cache:
        print("Oh hey, I know this one!")
        return factorial_cache[val]*mult
    else:
        if val < 0:
            return None
        else:
            result = rec_fact(val-1, mult*val)
            if mult == 1:
                factorial_cache[val] = result
            return result

# print(rec_fact(1))
# print(rec_fact(6))

assert rec_fact(6)  == 720
# assert rec_fact(1)  == 1
# assert rec_fact(0)  == 1
# assert rec_fact(-1) == None
print(rec_fact(100))
print(rec_fact(100))
print(rec_fact(10))

dic =  {0 : 1, 1: 1}
def factorial(n):
    if n < 0:
        return None
    if n not in dic:
        dic[n] = n * factorial(n - 1)
    return dic[n]
