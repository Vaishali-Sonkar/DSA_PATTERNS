// https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum

class Solution(object):
    def minStartValue(self, nums):
        sum =0
        minsum =0
        for i in range(len(nums)):
            sum += nums[i]
            minsum = min(sum,minsum)
        return 1-minsum