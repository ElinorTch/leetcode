# Link: https://leetcode.com/problems/build-array-from-permutation/

def buildArray(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    return [nums[nums[i]] for i in range(len(nums))]


if __name__ == "__main__":
    print(buildArray([5,0,1,2,3,4]))