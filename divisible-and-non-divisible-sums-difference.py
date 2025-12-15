# Link: https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/
def differenceOfSums(n, m):
    """
    :type n: int
    :type m: int
    :rtype: int
    """
    num1 = 0
    num2 = 0
    i = 1
    while i <= n:
        if i % m == 0:
            num2 = num2 + i
        else:
            num1 = num1 + i
        i = i + 1
    return num1 - num2

if __name__ == "__main__":
    print(differenceOfSums(10, 3))