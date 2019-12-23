a = "ab"
b= "b"
#check 
c= b in a
print(c)

ab = 'my %s' %('girl')
print(ab)

s = '%s %s'
result = s %('1','2')
print(result)

k = 'phuc'
result = f'{k} - abc'
print(result)

a = 'ab - nb - ok'
b = a.title()
print(b)

a = 'b'
b = a.center(30,'*')
c = a.ljust(5,"-")
d = a.rjust(5,"-")
print(b)
print(c)
print(d)