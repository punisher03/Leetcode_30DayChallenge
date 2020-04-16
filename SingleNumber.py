#Given a non-empty array of integers, every element appears twice except for one. Find that single one.

#using math

def check(a):
    s=sum(set(a))
    return 2*s-sum(a)
print(check([1,1,2,2,3,4,4,5,5]))
