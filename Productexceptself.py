class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero = 0;
        for num in nums:
            if num == 0:
                zero += 1
            else:
                product *= num
        for i in range(0, len(nums)):
            if zero == 0:
                nums[i] = product // nums[i]
            elif zero == 1 and nums[i] == 0:
                nums[i] = product
            else:
                nums[i] = 0
        return nums
