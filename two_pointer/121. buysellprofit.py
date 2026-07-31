class Solution(object):
    def maxProfit(self, prices):
        mp=0
        bp=prices[0]
        for i in range(1,len(prices)):
            sp=prices[i]
            if sp>bp:
                price=sp-bp
                mp=max(mp,price)
            else:
                bp=sp   #when the currnt day price is less than previous will hangethe buy date 
        return mp
        