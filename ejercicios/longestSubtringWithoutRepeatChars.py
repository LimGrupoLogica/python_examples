class Solution:
    def calculateLength(self, s: str) -> int:
        repeat = ""
        count = 0
        length = 1

        for x in s:
            repeat += x

            if repeat.count(x) > 1:
                if count > length:
                    length = count
                count = 0
            count += 1
        else: 
            if count > length:
                length = count
        return length


    def lengthOfLongestSubstring(self, s: str) -> int:
        print(f"length: {len(s)} {s.isspace()} split: ")
        if s == "": return 0
        if s.isspace(): return 1
        normal = self.calculateLength(s)
        reverseStr = self.calculateLength(s[::-1])
        print(f"normal: {normal} reverse: {reverseStr}, lists: {s[::-1]}")
        if normal > reverseStr:
            return normal
        else: 
            return reverseStr

                 
    
x = Solution()

print(x.lengthOfLongestSubstring("asjrgapa"))
#        print(f"normal: {normal} reverse: {reverseStr}, list: {strList}")

            #print(repeat.count(x))
#print(f"count {count} length: {length}")