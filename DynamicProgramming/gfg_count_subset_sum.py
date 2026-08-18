# class Solution:
# 	def perfectSum(self, arr, target):
# 		# code here
#         n = len(arr)
        
#         dp = [[0] * (target + 1) for _ in range(n + 1)]
        
#         dp[n][0]=1
#         for i in range(n-1,-1,-1):
#             for j in range(target + 1): 
#                 if arr[i]>j:
#                     dp[i][j]=dp[i+1][j]
#                 else:
#                     dp[i][j]=dp[i+1][j-arr[i]] + dp[i+1][j]
#         return dp[0][target]