class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for x in  s[::-1]:
            if  x != " ":
                hasWord = True
                length += 1
            if hasWord and x == " ":
                break
        return length
    
x =  Solution()
print(x.lengthOfLastWord("   fly me   to   the moon  "))