f1 = 1
f2 = f1
n = int(input())
for i in range(1, n+1):
    f1, f2 = f2, f2 + f1
    print(f2)
