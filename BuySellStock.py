prices=[1,2,3,4,5]
maxx=0
for i in range(1,len(prices)):
    if prices[i-1]<prices[i]:
        maxx+=prices[i]-prices[i-1]
print(maxx)
