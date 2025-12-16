# Link: https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/

def minimumOperations(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    counter = 0
    for num in nums:
        if num % 3 != 0:
            counter += 1
    return counter


if __name__ == "__main__":
    print(minimumOperations([1,2,3,4]))
