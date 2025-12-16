# Link:https://leetcode.com/problems/maximum-substrings-with-distinct-start/

def maxDistinct(s: str):
    """
    :type s: str
    :rtype: int
    """
    str_dict: dict = {}
    count: int = 0
    for value in s:
        if value not in str_dict:
            str_dict[value] = 1
            count = count + 1
    return count
    # return len(set(s))
            
    
if __name__ == "__main__":
    print(maxDistinct("aaaa"))
    