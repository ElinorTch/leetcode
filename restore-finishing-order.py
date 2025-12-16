# Link: https://leetcode.com/problems/restore-finishing-order/

def recoverOrder(order, friends):
    """
    :type order: List[int]
    :type friends: List[int]
    :rtype: List[int]
    """
    output = []
    for value in order:
        if value in friends:
            output.append(value)
        if len(output) ==  len(friends):
            break
    return output

if __name__ == "__main__":
    print(recoverOrder([1,4,5,3,2], [2,5]))
