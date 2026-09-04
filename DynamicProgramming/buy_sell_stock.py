class Solution(object):
    def func(self,prices,n,i,k):
        if i==n:
            return 0
        if k==0:
            return 0
        if k==2:
            c1=self.func(prices,n,i+1,k-1)-prices[i]
            c2=self.func(prices,n,i+1,k)
            return max(c1,c2)
        else:
            c1=self.func(prices,n,i+1,k-1)+prices[i]
            c2=self.func(prices,n,i+1,k)
            return max(c1,c2)
    def maxProfit(self, prices):
        k=2
        n=len(prices)
        dp
        return self.func(prices,n,0,k)

class Solution(object):
    def func(self,prices,n,i,k):
        if i==n:
            return 0
        if k==0:
            return 0
        if k==2:
            c1=self.func(prices,n,i+1,k-1)-prices[i]
            c2=self.func(prices,n,i+1,k)
            return max(c1,c2)
        else:
            c1=self.func(prices,n,i+1,2)+prices[i]
            c2=self.func(prices,n,i+1,k)
            return max(c1,c2)
    def maxProfit(self, prices):
        k=2
        n=len(prices)
        dp
        return self.func(prices,n,0,k)

class Solution(object):
    def func(self,prices,n,i,k):
        if i==n:
            return 0
        if k==0:
            return 0
        if k%2==0:
            c1=self.func(prices,n,i+1,k-1)-prices[i]
            c2=self.func(prices,n,i+1,k)
            return max(c1,c2)
        else:
            c1=self.func(prices,n,i+1,k-1)+prices[i]
            c2=self.func(prices,n,i+1,k)
            return max(c1,c2)
    def maxProfit(self, prices):
        k=4
        n=len(prices)
        dp
        return self.func(prices,n,0,k)

        