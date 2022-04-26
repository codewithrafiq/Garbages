# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         list = []
#         hate = None
#         for x, y in zip(l1, l2):
#             v = x + y
#             if hate:
#                 list.append(v+int(hate))
#             elif v < 10:
#                 list.append(x+y)
#             else:
#                 list.append(int(str(v)[-1]))
#                 hate = int(str(v)[0])
#         return list

# s = Solution().addTwoNumbers([2, 4, 3], [5, 6, 4])
# print(s)


from typing import Optional


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        strings = [str(integer) for integer in l1]
        a_string = "".join(strings)
        list_1 = int(a_string)

        strings = [str(integer) for integer in l2]
        a_string = "".join(strings)
        list_2 = int(a_string)

        final = [int(i) for i in str(list_1 + list_2)]
        return final[::-1]


s1 = Solution().addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9])
s2 = Solution().addTwoNumbers([2, 4, 3], [5, 6, 4])

print(s1)
print(s2)





# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        