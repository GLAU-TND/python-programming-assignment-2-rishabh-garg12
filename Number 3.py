a = bin(int(input('enter a number ')))
b = []
d = 0
for i in range (2,len(a)-1):
    if a[i] == a[i+1] and a[i] == '1':
        d += 1
        b.append(d)
    elif a[i+1] == '0':
        d = 0
c = len(b)
print(c+1)
