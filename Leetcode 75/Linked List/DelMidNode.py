from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return head


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
    head = listToListNode([1])
    solution = Solution()
    result = solution.deleteMiddle(head)
    print(listNodeToList(result))


if __name__ == "__main__":
    main()
