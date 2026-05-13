class Solution(object):
    def possibleStringCount(self, word):
        ans=1
        i=0
        while i<len(word):
            j=i
            while j<len(word) and word[j]==word[i]:
                j+=1
            length=j-i
            ans+=(length-1)
            i=j
        return ans