# Link: https://leetcode.com/problems/number-of-good-pairs/

def numIdenticalPairs(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # pair_table = {}
    # for i in nums:
    #     if pair_table.get(i):
    #         pair_table[i] = pair_table[i] + 1
    #     else:
    #         pair_table[i] = 1

    # possible_couple = 0
    # for i in pair_table.values():
    #     possible_couple += i * (i - 1) // 2

    # return possible_couple

    count=0
    hasdict={}
    for i in range(len(nums)):
        if nums[i] in hasdict:
            count+=hasdict[nums[i]]
            hasdict[nums[i]]+=1
        else:
            hasdict[nums[i]]=1
    return count    

print(numIdenticalPairs([1, 1, 1, 1]))    