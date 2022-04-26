
# l1 = [2,4,3]
# l2 = [5,6,4]

# def twoNumbers(l1,l2):
#     list1 = ""
#     list2 = ""
#     for a,b in zip(l1[::-1],l2[::-1]):
#         list1 += str(a)
#         list2 += str(b)
#     print(list1,list2)
#     listf = [l for l in str(int(list1) + int(list2))]
#     return  listf


# rsult = twoNumbers(l1,l2)

# print(rsult)





l1 = [9,9,9,9,9,9,9]
l2 =  [9,9,9,9]

def twoNumbers(l1,l2):
    list1 = ""
    list2 = ""
    for a,b in zip(l1[::-1],l2[::-1]):
        list1 += str(a)
        list2 += str(b)
    print(list1,list2)
    listf = [l for l in str(int(list1) + int(list2))]
    return  listf


rsult = twoNumbers(l1,l2)

print(rsult)