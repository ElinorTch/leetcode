# Link: https://leetcode.com/problems/concatenation-of-array/

def getConcatenation(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    return nums + nums

if __name__ == "__main__":
    print(getConcatenation([1,2,1]))