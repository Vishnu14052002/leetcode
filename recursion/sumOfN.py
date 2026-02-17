
def sumOfa(a):
    if a == 0:
        return 0
    return a + sumOfa(a - 1)


val = sumOfa(3)
print(val)
    