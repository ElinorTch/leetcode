# Link: https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next: ListNode = None):
        self.val = val
        self.next = next

def insertGreatestCommonDivisors(head: ListNode):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    current = head
    temp = None

    while current and current.next:
        if current.val < current.next.val:
            temp = ListNode(pgcd(current.next.val, current.val), current.next)
            current.next = temp
            current = temp.next

        else:
            temp = ListNode(pgcd(current.val, current.next.val), current.next)
            current.next = temp
            current = temp.next

    return head.val

    
def pgcd(i, j):
    if j == 0:
        return i
    else:
        return pgcd(j, i % j)

node1 = ListNode(18)
node2 = ListNode(6)
node3 = ListNode(10)
node4 = ListNode(3)

node1.next = node2
node2.next = node3
node3.next = node4

if __name__ == "__main__":
    print(insertGreatestCommonDivisors(node1))