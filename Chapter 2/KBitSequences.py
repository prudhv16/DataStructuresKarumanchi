#K bit sequence

def digitseq(k):
    return [str(x) for x in range(k)]

def kbitSqeunce(n,k):
    if n == 0: return []
    if n == 1: return digitseq(k)
    temp = []
    return [digit + bitstring for digit in kbitSqeunce(1,k) for bitstring in kbitSqeunce(n-1,k)]

print kbitSqeunce(2,3)