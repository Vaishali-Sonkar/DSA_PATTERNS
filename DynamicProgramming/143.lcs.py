# class Solution(object):
#     def lcs(self,text1,text2,n,m,i,j,dp):
#         if i==n or j==m:
#             return 0
#         if dp[i][j]!=-1:
#             return dp[i][j]
#         if text1[i]==text2[j]:
#             dp[i][j]=1+self.lcs(text1,text2,n,m,i+1,j+1,dp)
#             return dp[i][j]
#         c1=self.lcs(text1,text2,n,m,i+1,j,dp)
#         c2=self.lcs(text1,text2,n,m,i,j+1,dp)
#         dp[i][j]=max(c1,c2)
#         return dp[i][j]
#     def longestCommonSubsequence(self, text1, text2):
#         n=len(text1)
#         m=len(text2)
#         dp = [[-1] * (m + 1) for _ in range(n + 1)]
#         return self.lcs(text1,text2,n,m,0,0,dp)

class Solution(object):

    def longestCommonSubsequence(self, text1, text2):

        n = len(text1)
        m = len(text2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):

                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]

                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        return dp[0][0]