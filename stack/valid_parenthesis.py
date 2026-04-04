class Solution(object):
    def isValid(self, s):
        stack = [] # Yeh hamara stack hai
        
        for i in range(len(s)):
            char = s[i]
            
            # 1. Agar opening bracket hai, toh stack mein PUSH karo
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            
            # 2. Agar closing bracket hai, toh PEEK aur POP karo
            else:
                # Agar stack pehle se khali hai, matlab closing bracket bina pair ke hai
                if not stack:
                    return False
                
                top = stack.pop() # Top element bahar nikalo
                
                # Check karo ki kya pair sahi hai
                if char == ')' and top != '(':
                    return False
                if char == '}' and top != '{':
                    return False
                if char == ']' and top != '[':
                    return False
        
        # 3. Last mein agar stack khali hai, toh sab balanced hai
        return len(stack) == 0