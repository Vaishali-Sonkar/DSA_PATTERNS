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





#the TABULATION APPROACH -> Space Complexity o(1) ,lesser time no extra space used
class Solution(object):
    def fib(self, n):
        if n==0 or n==1:
            return n
        prev=1
        prev_1=0
        for i in range(2,n+1):
            ans=prev+prev_1
            prev_1=prev
            prev=ans
        return ans