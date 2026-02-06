m = int(input("Enter m: "))
n = int(input("Enter n: "))
d = {}
for i in range(m, n + 1):
    d[i] = i * i
print(d)
