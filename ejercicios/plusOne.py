class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digStr = str(digits)
        digStr.replace(",", "")
        nums = int(digStr) + 1

        return nums
    

x = Solution()
print(x.plusOne())