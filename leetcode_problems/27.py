from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_list = [str(i) for i in nums]
        int_list = []
        str_list = []
        for l in list(map(lambda x: x.replace(str(val), ' '), new_list)):

        final_list = sorted(int_list)
        return final_list + str_list


s = Solution().removeElement([3, 2, 2, 3], 3)
print(s)
