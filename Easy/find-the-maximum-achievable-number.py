# Link: https://leetcode.com/problems/find-the-maximum-achievable-number/

def theMaximumAchievableX(num, t):
    """
    :type num: int
    :type t: int
    :rtype: int
    """
    return num + t + t

if __name__ == "__main__":
    print(theMaximumAchievableX(3, 2))