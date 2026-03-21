class Solution(object):
    def minSubArrayLen(self, target, nums):   # O(n) time, O(1) space
        low=0
        ans=float('inf')
        s=0
        for high in range(0,len(nums)):  
            s+=nums[high]
            while s>=target:                  # When we have a valid window, try to shrink it from the left
                l=high-low+1                   # Calculate the length of the current valid window and update the answer
                ans=min(l,ans)      
                s-=nums[low]                  # Remove the leftmost element from the sum and move the low pointer to the right
                low+=1
        return ans if ans != float('inf') else 0       # If ans is still infinity, it means we never found a valid window, so return 0

