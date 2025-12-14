# Link: https://leetcode.com/problems/score-of-a-string/

def scoreOfString(s):
    """
    :type s: str
    :rtype: int
    """
    return sum(abs(ord(s[i]) - ord(s[i + 1])) for i in range(len(s) - 1))

if __name__ == "__main__":
    print(scoreOfString("hello"))