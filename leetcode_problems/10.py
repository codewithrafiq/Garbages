import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        result = re.findall(p,s)
        print(result)
        if len(result) <
        if result is None:
            return False
        else:
            return True


s = Solution().isMatch('aa','a')
print(s)
