def oneton(n):
    ls=[True for i in range(n+1)]
    i=2
    while i*i<=n:
        if ls[i]==True:
            k=i*i
            while k<=n:
                ls[k]=False
                k+=i
        i+=1
    x=[i for i in range(2,n+1) if ls[i]]
    return x
l,r=map(int,input().split())
if l<=1:
    l=2
m = int(r**0.5)
ls = oneton(m)
print(ls)
arr = {i:True for i in range(l,r+1)}
x=0
c=0
while x<len(ls):
    if l%ls[x]!=0:
        sp = ((l // ls[x])+1) * ls[x]
        if sp==ls[x]:
            sp+=ls[x]
    else:
        sp=l
        if sp==ls[x]:
            sp+=ls[x]
        
    while sp<=r:
        arr[sp]=False
        sp+=ls[x]
    x+=1
for i in arr:
    if arr[i]:
        print(i,end=' ')
