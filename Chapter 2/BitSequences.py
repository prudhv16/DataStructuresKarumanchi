#Bit sequencies

def elemadder(elem,List):
    return ["".join([elem,item]) for item in List]

def bitSequencies(n):
    if n == 0: return []
    if n == 1: return ["0","1"]
    return elemadder("0",bitSequencies(n-1)) + elemadder("1",bitSequencies(n-1))

print bitSequencies(2)