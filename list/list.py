a = [i for i in range(30)]
print(a)

a = [[n, n*1, n*2] for n in range(1,4)]
print(a)

a = [1,2,3]
b = list(a)
print(b)
print(a)
b[0] = 'A'
print(b)
print(a)
print('\n')

a = [1,1,2,3]
b = a.count(1)
c = a.index(2)
a.append(4)
a.extend([5,6])
#a.insert(2,3)
print(b,'-',c,'-',a)
print('\n')
