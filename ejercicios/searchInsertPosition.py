class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        nums.sort()
        c = 0
        result = 0
        if target > nums[len(nums) - 1]:
            return len(nums)
        
        for x in range(len(nums)):
           
            if nums[x] == target:
                result = x
                break
            if target < nums[x] and target > nums[x - 1]:
                result = x 
                break

           

        return result
    

x = Solution()
print(x.searchInsert(nums = [1,3,5,6], target = 2))