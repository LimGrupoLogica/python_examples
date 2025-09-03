class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0: return "" 
        o = ""
        c = 1

        for x in strs[0]:
            for i in strs[1:]:
                if x in i and o + x in i and i.startswith(o + x):
                    c += 1
                
            if c == len(strs):
                o += x
            else:
                break
            c = 1


        return o
    
x = Solution()
print(x.longestCommonPrefix(["c","acc","ccc"]))