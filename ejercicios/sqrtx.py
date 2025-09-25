class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0

        if x == 2: return 1
        raiz = 1

        for i in range(1, x):
            if i * i == x:
                raiz = i
                break
            elif i * i > x:
                raiz  = i - 1
                break

        return raiz


o = Solution()
print(o.mySqrt(4))