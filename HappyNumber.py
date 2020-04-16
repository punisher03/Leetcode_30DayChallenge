s=int(input())
check=[]
def squareit(s):
    p=0
    while(s>0):
        m=s%10
        p+=m**2
        s//=10
    return p
k=squareit(s)
while(k not in check):
    if k==1:
        print("True")
        break
    check.append(k)
else:
    print("False")
