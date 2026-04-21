class Solution(object):
    def longestPalindrome(self, s):
        f=Counter(s)            #tales the freq and stores it in a dictionary
        res=0            
        odd=False               #flag to check if there is any odd frequency character
        for i in f:
            val=f[i]            
            if(val%2==0):          #all even then eaisly taking pair of characters 
                res+=val            #even no of characters can be fully used in palindrome
            else:                      
                res+=val-1            #takes even num in pairs 1 character will be left out
                odd=True          
        if(odd==False):
            return res
        return res+1              #any 1 left out char in center of palindrome , no matter which char it is , only 1 char can be added 
# The time complexity of this solution is O(n) because we need to iterate through the string to count the frequency of each character, and then iterate through the frequency dictionary to calculate the length of the longest palindrome. The space complexity is O(1) because the frequency dictionary will have at most 26 entries for lowercase letters (or 52 for both uppercase and lowercase letters).
