class Solution(object):
    def maxProduct(self, nums):
        min_prod=nums[0]
        max_prod=nums[0]
        res=nums[0]
        # we have to consider the case when the current element is the max or min product
        for i in range(1,len(nums)):
            vi=nums[i]
            vii=max_prod*nums[i]
            viii=min_prod*nums[i]
            max_prod=max(vi,max(vii,viii))
            min_prod=min(vi,min(vii,viii))
            res=max(res,max(max_prod,min_prod))

        return res


        