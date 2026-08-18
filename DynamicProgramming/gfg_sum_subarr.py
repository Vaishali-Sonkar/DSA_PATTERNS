class Solution:
    def func(self, arr, n, sum1, i, dp):

        if i == n:
            if sum1 == 0:
                return True
            return False

        if dp[i][sum1] != -1:
            return dp[i][sum1]

        # If current element is bigger than sum,
        # we cannot take it
        if arr[i] > sum1:
            dp[i][sum1] = self.func(arr, n, sum1, i + 1, dp)
            return dp[i][sum1]

        c1 = self.func(arr, n, sum1 - arr[i], i + 1, dp)
        c2 = self.func(arr, n, sum1, i + 1, dp)

        dp[i][sum1] = c1 or c2

        return dp[i][sum1]

    def isSubsetSum(self, arr: list[int], sum: int) -> bool:
        n = len(arr)

        dp = [[-1] * (sum + 1) for _ in range(n + 1)]

        return self.func(arr, n, sum, 0, dp)
        
        
#TABULATION METHOD
    def isSubsetSum(self, arr: list[int], sum: int) -> bool:
        n = len(arr)

        dp = [[0] * (sum + 1) for _ in range(n + 1)]

        dp[n][0]=1
        for i in range(n-1,-1,-1):
            for j in range(sum + 1):
                if arr[i]>j:
                    dp[i][j]=dp[i+1][j]
                else:
                    dp[i][j]=dp[i+1][j-arr[i]] or dp[i+1][j]
        return dp[0][sum]
                    