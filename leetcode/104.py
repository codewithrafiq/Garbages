# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

s = Solution()
ddd = [3,9,20,None,None,15,7]
print(s.maxDepth(ddd))


