from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head or not head.next:
            return None
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
            print(fast, tmp.val, slow.val, prev.val)
        res = 0
        while slow:
            res = max(res, slow.val + prev.val)
            slow = slow.next
            prev = prev.next
        return res


def listToListNode(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def listNodeToList(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def main():
    head = listToListNode([5, 4, 2, 1])
    solution = Solution()
    result = solution.pairSum(head)
    print(result)


if __name__ == "__main__":
    main()
