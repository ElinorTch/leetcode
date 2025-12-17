# Link:  https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

def minOperations(boxes):
    """
    :type boxes: str
    :rtype: List[int]
    """
    n = len(boxes)
    res = [0 for _ in range(n)]

    b = 0
    m = 0
    for i in range(n):
        res[i] += m
        if boxes[i] == '1':
            b += 1 
        m += b
    
    b = 0
    m = 0
    for i in range(n-1,-1,-1):
        res[i] +=m
        if boxes[i] == '1':
            b +=  1
        m += b
    return res


if __name__ == "__main__":
    print(minOperations("001011"))