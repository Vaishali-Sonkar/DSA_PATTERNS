class Solution:
    def twoSum(self, numbers, target):
        low = 0
        high = len(numbers) - 1

        while low < high:
            s = numbers[low] + numbers[high]

            if s == target:
                return [low + 1, high + 1]
            elif s < target:
                low += 1
            else:
                high -= 1


# 🔹 Test the function (optional for VS Code)
if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9

    sol = Solution()
    result = sol.twoSum(numbers, target)

    print("Indices:", result)