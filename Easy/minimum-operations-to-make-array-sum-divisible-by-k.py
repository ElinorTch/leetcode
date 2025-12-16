# Link: https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k

def minOperations(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    total = sum(nums)
    near_multiple = int(total / k) * k
    return total - near_multiple
    
if __name__ == "__main__":
    print(minOperations([3, 9, 7], 5))
