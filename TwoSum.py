class Solution:
    def twoSum(nums,target):
        resultado = []
        if (len(nums)>2):
            for indice in range(len(nums)):
                for indice2 in range(len(nums)):
                    if nums[indice] + nums[indice2] == target and indice != indice2 and len(resultado)<=1:
                        resultado.append(indice)
                        resultado.append(indice2)
                        break  
        elif len(nums)==2:
            if nums[0]+nums[1]==target:
                resultado=[0,1]
        return resultado
   
print(Solution.twoSum([2,7,11,15],9))
   
   
   
   
   
   
   
   
