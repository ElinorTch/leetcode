# Link: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

def finalValueAfterOperations(operations):
    """
    :type operations: List[str]
    :rtype: int
    """
    x = 0
    for operation in operations:
        if "-" in operation:
            x -= 1
        else:
            x += 1
    return x

if __name__ == "__main__":
    print(finalValueAfterOperations(["++X","++X","X++"]))