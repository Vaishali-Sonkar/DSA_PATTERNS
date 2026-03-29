#https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution(object):
    def subarraysDivByK(self, nums, k):
        f={0:1}
        s=0      #inital sum of the subarray
        res=0    
        for num in nums:
            s+=num
            rem=s%k      #the remainder when the sum is divided by k
            if rem<0:     #if rem is -ve, we need to add k to make it positive 
                rem=rem+k   
            if rem in f:     #check if rem exist in dict-(f)
                res+=f[rem]   #if it exists, add the frequency of that rem to the result
                f[rem]+=1      #update the frequency of the rem in the dict
            else:
                f[rem]=1     #if rem does not exist in the dict, add it with frequency 1
        return res       