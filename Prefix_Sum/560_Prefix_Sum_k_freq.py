class Solution(object):
    def subarraySum(self, nums, k):
        f={}  #initalize a dict to store the frequency of prefix sums
        s=0   #set the initial prefix sum to 0
        f[0]=1  #empty prefix sum has a frequency of 1 only
        res=0    #count of subarrays with sum k
        for i in range(len(nums)):
            s+=nums[i]      #add the current number to the prefix sum
            ques=s-k           #the prefix sum we need to find in the dict to get a subarray with sum k
            if ques in f:         #check if the required prefix sum exists in the dict
                res+=f[ques]     #if it exists, add the frequency of that prefix sum to the result
            f[s]=f.get(s,0)+1      #freq update for the current prefix sum
        return res