from itertools import permutations
s = list(map(str,input().split()))
l = list(permutations(s))
max = 0
for i in l:
    a = ""
    for j in i:
        a = a+j
    if int(a) > max:
        max = int(a)
print(max)
    
