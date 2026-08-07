class Solution(object):
    def func(self,nums,n,i,free):
        if i==n:
            return 0
        if free==0:
            return self.func(nums,n,i+1,1)
        c1=nums[i]+ self.func(nums,n,i+1,0)
        c2=self.func(nums,n,i+1,1)
        return max(c1,c2)
    def rob(self, nums):
        n=len(nums)
        return self.func(nums,n,0,1)
#⬆️⬆️⬆️⬆️⬆️⬆️ this code will show time limit exceeded for large input because we are solving the same subproblems multiple times, we can use dp to optimize it

class Solution(object):
    def func(self,nums,n,i,free,dp):
        if i==n:
            return 0
        if dp[i][free]!=-1:
            return dp[i][free]
        if free==0:
            dp[i][free]=self.func(nums,n,i+1,1,dp)
            return dp[i][free]
        c1=nums[i]+self.func(nums,n,i+1,0,dp)
        c2=self.func(nums,n,i+1,1,dp)
        dp[i][free]=max(c1,c2)
        return dp[i][free]
    def rob(self, nums):
        n=len(nums)
        dp=[[-1]*2 for _ in range(n)]
        return self.func(nums,n,0,1,dp)
#this approach is dp with 2d array, we can optimize it to 1d array because we are only using the previous row of dp array
