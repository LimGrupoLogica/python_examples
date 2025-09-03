class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = nums.copy()

        for x in k:
            if nums.count(x) > 1:
                nums.remove(x)

        nums.sort()

        return len(nums)
    
