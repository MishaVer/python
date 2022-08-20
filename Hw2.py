from calendar import c


print('Hello world')
a = [2, 2, 3, 2, 5, 10, 7, 2]
b = a[::-1]
c = [x*y for x, y in zip(a, b)]
print(c)
n = len(c)
print(n)
if n % 2 == 0:
    fin_list = c[0:n//2]
    print(fin_list)
else:
    fin_list = c[0:(n//2) + 1]
    print(fin_list)