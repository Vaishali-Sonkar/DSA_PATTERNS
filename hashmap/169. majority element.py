from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        hm=Counter(nums)
        for key,val in hm.items():
            if val>len(nums)//2:
                return key

        
        