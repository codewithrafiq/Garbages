
# def twoSum(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     for i in range(0,len(nums)):
#         if nums[i] + nums[i+1]==target:
#             return [i,i+1]


# print(twoSum([2,7,11,15], 9))

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dic = {}
    for i,n in enumerate(nums):
        diff = target-n
        if diff in dic:
            return [dic[diff],i]
        dic[n]=i
    return


# print(twoSum([2,7,11,15], 9))


dic = {
    0:1
}

print(1 in dic)


# print([i for i in enumerate([2,7,11,15])])