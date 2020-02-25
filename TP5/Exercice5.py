def boolean_tuples(n) :
    ret = [(),]
    for i in range(n) :
        tmp = []
        for j in ret :
            tmp.append(j + (True,))
            tmp.append(j + (False,))
        ret = tmp
    return (ret)

def proposition(a, b, c) :
    return (not b or (not a and c)) and (c and a)

def SAT(f, n) :
    lst = boolean_tuples(n)
    for elem in lst :
        if f(*elem) :
            return elem
    return (None)

print(boolean_tuples(3), "\n")
print(SAT(proposition, 3))
