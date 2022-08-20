li_list = []
p_list = [12.35, 11.45, 23.56, 15.94, 45.4, 32.02, 1.11]
for i in p_list:
    print('%.2f' % i)
    li_list.append('%.2f' % i)
    print(li_list)
a_list = map(str, li_list)
b_list = [x.split('.')[1] for x in a_list]
print(b_list)
c_list = min(b_list)
d_list = max(b_list)
print(c_list)
print(d_list)
gmax = int(d_list)
gmin = int(c_list)
f = gmax - gmin
print(f)