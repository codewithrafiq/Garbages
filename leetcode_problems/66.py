# class Solution(object):
#     def plusOne(self, digits):
#         """
#         :type digits: List[int]
#         :rtype: List[int]
#     """
#         last = digits[-1]+1
#         final = digits[:-1]
#         for l in str(last):
#             final.append(int(l))
#         return final


from string import digits
from unicodedata import digit


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
    """

        strings = [str(integer) for integer in digits]
        a_string = "".join(strings)
        an_integer = int(a_string) + 1
        
        return [int(item) for item in list(str(an_integer))]


s = Solution().plusOne([9,9])
print(s)
