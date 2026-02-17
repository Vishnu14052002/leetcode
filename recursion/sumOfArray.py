def sumOfArray(n):
    if n == 0: return a[0]
    return a[n] + sumOfArray(n - 1)
a = [1,2,3]
val = sumOfArray(len(a)-1)
print(val)