class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        import os
        common = os.path.commonprefix(strs)
        return common

        


s = Solution().longestCommonPrefix(["flower","flow","flight"])
print(s)