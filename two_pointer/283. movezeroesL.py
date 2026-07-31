class Solution(object):
    def moveZeroes(self, nums):
        l=0
        for h in range(0,len(nums)):
            if nums[h]!=0:
                nums[l],nums[h]=nums[h],nums[l]
                l+=1
        return nums
        