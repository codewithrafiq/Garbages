class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(0, int(len(s)/2)):
            s = s.replace("()", "")
            s = s.replace("{}", "")
            s = s.replace("[]", "")

        if len(s) == 0:
            return True
        else:
            return False



s = Solution().isValid("(]")