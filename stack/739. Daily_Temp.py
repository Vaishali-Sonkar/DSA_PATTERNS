class Solution(object):
    def dailyTemperatures(self, temperatures):
        n=len(temperatures)
        res=[0]*n     
        stack=[]          # this stack will store the indices of the temperatures array
        for i in range(n-1,-1,-1):
            while stack and temperatures[stack[-1]]<= temperatures[i]:   #compare the current temperature with the temperature at the index on top of the stack
                stack.pop()              #current temperature is less than or equal to the temperature at the index on top of the stack, so we pop the stack
                res[i]=stack[-1]-i          #if the stack is not empty after popping, we calculate the number of days until a warmer temperature by taking the difference between the current index and the index on top of the stack
            stack.append(i)               #add the current index to the stack
        return res
# The time complexity of this solution is O(n) because each index is pushed and popped from the stack at most once. The space complexity is also O(n) in the worst case when all temperatures are in decreasing order, resulting in all indices being stored in the stack.