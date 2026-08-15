from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        count=Counter(nums)
        for key,val in count.items():
            if val==1:
                return key
        