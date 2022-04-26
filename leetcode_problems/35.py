class Solution:
    def searchInsert(self, nums, target):
        index = 0
        for i in nums:
            if(i == target or i > target):
                return index
            index = index+1
        return index



s = Solution().searchInsert([1,3, 5], 4)
print(s)
