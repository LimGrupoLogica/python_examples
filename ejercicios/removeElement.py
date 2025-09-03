class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = nums.copy()
        for x in k:
            if x == val:
                nums.remove(x)

        return len(nums)
    
x = Solution()
print(x.removeElement([0,1,2,2,3,0,4,2], 2))