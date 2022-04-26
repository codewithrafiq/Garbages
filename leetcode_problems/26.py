
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        dup_num = 0
        for i in nums:
            if i not in result:
                result.append(i)
            else:
                dup_num += 1

        nums = sorted(result)

        return dup_num, nums


print(Solution().removeDuplicates([1, 2, 12, 12, 12]))
