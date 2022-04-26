class Solution:
    def reverse(self, x: int) -> int:
        if '-' not in str(x):
            out1 =  int(str(x)[::-1])
            if not -2147483648 < out1 < 2147483648:
                return 0
            return out1
        else:
            s1 = str(x)[1:]
            out2 =  int(s1[::-1])-(int(s1[::-1])*2)
            if not -2147483648 < out2 < 2147483648:
                return 0
            return out2

s = Solution().reverse(-78)
print(s)