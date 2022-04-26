from unittest import result


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(s)):
            if i+1 != len(s) and roman[s[i]] < roman[s[i+1]]:
                result = result - roman[s[i]]
            else:
                result = result + roman[s[i]]
        return result


x = Solution().romanToInt("IV")
print(x)
