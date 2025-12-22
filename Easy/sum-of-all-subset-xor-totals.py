# Link: https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/

def subsetXORSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    result = []
    XOR = 0

    def backtrack(start, path):
        result.append(list(path))        
        
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(0, [])
    return result

if __name__ == "__main__":
    print(subsetXORSum([5, 1, 6]))