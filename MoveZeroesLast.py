n=[0,1,0,3,12]
index_nonzero=0
for i in range(len(n)):
    if n[i]!=0:
        n[index_nonzero]=n[i]
        index_nonzero+=1
for i in range(index_nonzero,len(n)):
    n[i]=0
print(n)
