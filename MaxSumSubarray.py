n=[-2,1,-3,4,-1,2,1,-5,4]
for i in range(1,len(n)):
    if n[i-1]>0:
        n[i]+=n[i-1]
print(max(n))
