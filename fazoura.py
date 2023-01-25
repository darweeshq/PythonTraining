a = [1,3,3,5,7,1]
b = []
c = []
rangeA = len(a)
for i in range(rangeA):
    if i==0:
        if a[i]>a[i+1]:
            b.append(1)
        else:
            b.append(0)
    if i>0 and i != rangeA-1:
        if a[i]>a[i+1] or a[i]>a[i-1]:
            b.append(1)
        else:
            b.append(0)
    if i == (rangeA-1):
         if a[i] > a[i - 1]:
             b.append(1)
         else:
             b.append(0)
for i in range(rangeA):
    count = 0
    j = i+1
    v =0
    for j in range(j,rangeA):
        if b[i]==0:
            break
        if b[j]==0:
            v= v
            break
        if b[i]>0 and b[j]==b[i]:
            v = v + 1
    c.append(v + b[i])
z = 0
for i in range(rangeA):
   z = z + c[i]

print(a)
print(b)
print(c)
print(z+rangeA)