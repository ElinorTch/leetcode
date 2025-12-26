# Link: https://leetcode.com/problems/partition-array-according-to-given-pivot/

def pivotArray(nums, pivot):
    """
    :type nums: List[int]
    :type pivot: int
    :rtype: List[int]
    """
    equal = []
    less_than = []
    greater_than = []

    for i in nums:
        if i < pivot:
            less_than.append(i)
        elif i > pivot:
            greater_than.append(i)
        else:
            equal.append(i)

    return less_than + equal + greater_than

print(pivotArray([-3,4,3,2], 2))