class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        c=0
        dic={0:-1}
        maxi=0
        for i in range(len(nums)):
            if nums[i]==1:
                c+=1
            else:
                c-=1
            if c in dic:
                maxi= max(maxi,i-dic[c])
            else:
                dic[c]=i

        return maxi
