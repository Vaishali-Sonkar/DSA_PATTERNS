class Solution(object):
    def func(self,n):
        if n<=1:
            return n
        if self.dp[n]!=-1:   #if the value of fib(n) is already calculated then return it from dp array
            return self.dp[n]
        self.dp[n]=self.func(n-1)+self.func(n-2)
        return self.dp[n]  #return last calculated value of fib(n)

    def fib(self, n):
        self.dp=[-1]*(n+1)  #creating array with -1 to save the values of fib(n) for n=0 to n
        return self.func(n)
        