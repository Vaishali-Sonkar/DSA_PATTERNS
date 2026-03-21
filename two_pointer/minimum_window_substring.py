class Solution(object):
    def minWindow(self, s, t):  # O(n) time, O(m) space where n is the length of s and m is the length of t
        if not s or not t:          # If either s or t is empty, we cannot find a valid window, so we
            return ""               # return an empty string

        need = Counter(t)              # Create a counter to keep track of the characters we need to find in s to form a valid window
        missing = len(t)              # Initialize the number of characters we are missing to form a valid window as the length of t                            
        left = start = end = 0         # Initialize the left pointer and the start and end indices of the minimum window found so far

        for right, ch in enumerate(s, 1):   # Iterate through the characters in s with their indices, starting from 1 for the right pointer
            if need[ch] > 0:                 # If the current character is needed to form a valid window, we decrease the missing count by 1
                missing -= 1
            need[ch] -= 1                     # Decrease the count of the current character in the need counter, even if it's not needed, to keep track of how many times it appears in the current window

            if missing == 0:                       # If we have found a valid window (missing is 0), we try to shrink it from the left to find the minimum window
                while left < right and need[s[left]] < 0:             # While the left pointer is less than the right pointer and the character at the left pointer is not needed (its count in need is negative), we can safely move the left pointer to the right to shrink the window
                    need[s[left]] += 1                # Increase the count of the character at the left pointer in the need counter, as we are moving past it and it may be needed again in the future
                    left += 1                 # Move the left pointer to the right

                if end == 0 or right - left < end - start:           # If we haven't found any valid window yet (end is 0) or the current valid window is smaller than the previously found minimum window, we update the start and end indices of the minimum window
                    start, end = left, right                          # Update the start and end indices of the minimum window found so far

                need[s[left]] += 1                     # After updating the minimum window, we need to move the left pointer to the right to look for the next valid window. Before moving the left pointer, we increase the count of the character at the left pointer in the need counter, as we are moving past it and it may be needed again in the future. We also increase the missing count by 1, as we are now missing one more character to form a valid window.
                missing += 1                             # Move the left pointer to the right to look for the next valid window
                left += 1                               # Move the left pointer to the right to look for the next valid window

        return s[start:end]                      # Return the minimum window substring found, which is the substring of s from index start to index end (exclusive). If no valid window was found, start and end will both be 0, and s[0:0] will return an empty string.
        