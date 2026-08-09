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


#the TABULATION APPROACH 
class Solution(object):
    def climbStairs(self, n):
        if n==0 or n==1:
            return 1
        prev=1
        prev1=0
        for i in range(2,n+2):
            ways=prev+prev1
            prev1=prev
            prev=ways
        return ways