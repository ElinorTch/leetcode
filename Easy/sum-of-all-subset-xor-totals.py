# Link: https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/

def subsetXORSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    result = [0] 
    def backtrack(nums,path,index,xor_sum):
        result[0] += xor_sum
        for i in range(index,len(nums)):
            backtrack(nums,path,i+1,xor_sum^nums[i])
    backtrack(nums,[],0,0)
    return result[0]

if __name__ == "__main__":
    print(subsetXORSum([3,4,5,6,7,8]))