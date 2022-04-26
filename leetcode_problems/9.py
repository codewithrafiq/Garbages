class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = list(str(x))
        if x == x[::-1]:
            return True
        else:
            return False


s = Solution().isPalindrome("21")
print(s)
