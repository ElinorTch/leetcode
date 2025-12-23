# Link: https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

def getSneakyNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    dict = {}
    ans = []
    for i in nums:
        if dict.get(i):
            ans.append(i)
            continue
        dict[i] = 1
    
    return ans

print(getSneakyNumbers([7,1,5,4,3,4,6,0,9,5,8,2]))