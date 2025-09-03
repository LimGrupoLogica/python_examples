class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] == ")" or s[0] == "]" or s[0] == "}": return False
        closes = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        hasPair = False
        charOpen = []
        unPair = []
        
        for c in s:
            if c == "(" or c == "[" or c == "{":
                hasPair = False
                charOpen.append(c)
            elif len(charOpen) > 0 and (c == ")" or c == "]" or c == "}"):
                hasPair = False
                if  c == closes[charOpen[-1]]:
                    charOpen.pop()
                    if len(charOpen) == 0 : hasPair = True
                else:
                    hasPair = False
                    break
            else:
                unPair.append(c)
                hasPair = False

        return hasPair and len(unPair) == 0
    

x = Solution()
print(x.isValid("([)]"))