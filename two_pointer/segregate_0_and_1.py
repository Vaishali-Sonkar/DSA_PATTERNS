"""
Problem: Segregate 0s and 1s in an array

Approach:
---------
Use the Two Pointer technique:
- Place one pointer (low) at the start
- Place another pointer (high) at the end
- Move pointers inward based on conditions:
    - If arr[low] is 0 → move low forward
    - If arr[high] is 1 → move high backward
    - Else swap both elements

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def segregate0and1(self, arr):
        low = 0
        high = len(arr) - 1

        while low < high:
            if arr[low] == 0:
                low += 1
            elif arr[high] == 1:
                high -= 1
            else:
                # Swap incorrect elements
                arr[low], arr[high] = arr[high], arr[low]
                low += 1
                high -= 1

        return arr


# 🔹 Driver Code (for testing in VS Code)
if __name__ == "__main__":
    arr = [0, 1, 1, 0, 1, 0]

    sol = Solution()
    result = sol.segregate0and1(arr)

    print("Input Array:  [0, 1, 1, 0, 1, 0]")
    print("Output Array:", result)