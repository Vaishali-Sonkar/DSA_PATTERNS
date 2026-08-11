class Solution:

    def func(self, arr, n, i, target, dp):

        # Target achieved
        if target == 0:
            return True

        # No elements remaining
        if i == n:
            return False

        # Target became negative
        if target < 0:
            return False

        # Already calculated
        if dp[i][target] != -1:
            return dp[i][target]

        # Take current element
        take = self.func(
            arr, n, i + 1,
            target - arr[i],
            dp
        )

        # Don't take current element
        not_take = self.func(
            arr, n, i + 1,
            target,
            dp
        )

        dp[i][target] = take or not_take

        return dp[i][target]

    def isSubsetSum(self, arr, target):

        n = len(arr)

        dp = [[-1] * (target + 1) for _ in range(n)]

        return self.func(arr, n, 0, target, dp)