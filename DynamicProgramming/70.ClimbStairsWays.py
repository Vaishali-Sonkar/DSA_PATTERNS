class Solution(object):
    def func(self,n):
        if n<=1:
            return 1
        if self.dp[n]!=-1:
            return self.dp[n]
        self.dp[n]=self.func(n-1)+self.func(n-2)
        return self.dp[n]
    def climbStairs(self, n):
        self.dp=[-1]*(n+1)
        return self.func(n)