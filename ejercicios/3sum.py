class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        out = []
        i = 0
        j = 1
        k = 2
    
        while i <= len(nums) -3:
            if k == len(nums):
                break
            
            triplet = list([nums[i],nums[j],nums[k]])
            if nums[i] ==  -66:

                print(triplet)
            triplet.sort()
            if nums[i] + nums[j] + nums[k] == 0 and triplet not in out:
                out.append(triplet)
            k += 1
            
            if k == len(nums):
                j += 1
                k = j + 1
            if j == len(nums) -1:
                i += 1
                j = i + 1
                k = j + 1
            
                
        return out
    
x = Solution()
print(x.threeSum([34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]))
            

"""  out.sort()
        for x in out:
            x.sort()
            if x not in out2:
                out2.append(x)
         """




""" 

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        out = []
        out2 = []

        for a in range(len(nums)):
            for b in range(1, len(nums)):
                for c in range(2, len(nums)):
                    if a != b and a != c and b != c:
                        if nums[a] + nums[b] + nums[c] == 0:
                            out.append([nums[a], nums[b], nums[c]])

        out.sort()
        for x in out:
            x.sort()
            if x not in out2:
                out2.append(x)
        
      
        return out2
 """