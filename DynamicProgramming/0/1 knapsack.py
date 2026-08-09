class Solution:
    def func(self, w, val, wt, i, n, dp):
        if i == n:
            return 0

        if dp[i][w] != -1:
            return dp[i][w]

        if wt[i] > w:
            dp[i][w] = self.func(w, val, wt, i + 1, n, dp)
            return dp[i][w]
        yes = val[i] + self.func(
            w - wt[i], val, wt, i + 1, n, dp
        )
        no = self.func(
            w, val, wt, i + 1, n, dp
        )

        dp[i][w] = max(yes, no)

        return dp[i][w]

    def knapsack(self, W, val, wt):
        n = len(wt)
        dp = [[-1] * (W + 1) for _ in range(n)]

        return self.func(W, val, wt, 0, n, dp)
        
        
        
class Solution:
    def knapsack(self, W, val, wt):

        dp = [0] * (W + 1)

        for i in range(len(wt)):

            for w in range(W, wt[i] - 1, -1):

                dp[w] = max(
                    dp[w],
                    val[i] + dp[w - wt[i]]
                )

        return dp[W]