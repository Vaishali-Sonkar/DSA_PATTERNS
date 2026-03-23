class Solution(object):
    def maxSubArray(self, nums):
        be=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            vi=be+nums[i]
            vii=nums[i]
            be=max(vi,vii)
            ans=max(ans,be)
        return ans

        