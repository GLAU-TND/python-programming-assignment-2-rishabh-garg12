a = list(input('enter only string ').split())
c = []
d = 0
c.append(a[0])
for i in range (len(a)-1):
    d = 0
    for j in range (i,len(a)-1):
        b = len(a[i])
        if a[i][b-1] == a[j+1][0]:
            d +=1
            if d == 1:
                c.append(a[j+1])
                a.insert((len(c)-1),a[j+1])
                a.pop(j+2)
print(c)
